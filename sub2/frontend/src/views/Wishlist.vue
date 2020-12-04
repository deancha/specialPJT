<template>
  <div style="margin: 50px 0">
    <div class="col-lg-12 order-1 order-lg-2 products-part">
      <div class="product-list">
        <table class="product-item">
          <thead>
            <tr>
              <th style="padding: 10px">
                <input type="checkbox" @click="checkAll" v-model="allChecked" />
              </th>
              <th>이미지</th>
              <th>상품명</th>
              <th>수량</th>
              <th>금액</th>
              <th>삭제</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="!liquor || liquor.length == 0">
              <td colspan="6">담은 상품이 없습니다.</td>
            </tr>
            <tr
              class="col-lg-4 col-sm-6"
              v-for="liquor in liquor"
              :key="liquor.cart_id"
            >
              <td class="bc-item">
                <input
                  type="checkbox"
                  v-model="check"
                  :value="liquor.cart_id"
                />
              </td>
              <td class="pi-pic">
                <img :src="'img/liquor/a' + liquor.liquornumber + '.jpg'" />
              </td>
              <td class="pi-text">
                <a :href="'#/detail/' + liquor.liquornumber">
                  <h5>{{ liquor.liquorname }}</h5>
                </a>
              </td>
              <td class="qua-col">
                <i
                  class="fa fa-minus"
                  @click="liquor.quantity > 1 ? (liquor.quantity -= 1) : ''"
                ></i>
                <span style="margin: 0 15px">{{ liquor.quantity }}</span>
                <i class="fa fa-plus" @click="liquor.quantity += 1"></i>
              </td>
              <td class="product-price">
                {{ (liquor.liquorprice * liquor.quantity).toLocaleString() }}원
              </td>
              <td>
                <i
                  class="fa fa-remove"
                  @click="deleteLiquor(liquor.cart_id)"
                ></i>
              </td>
            </tr>
            <!-- <infinite-loading
              v-if="loading"
              @infinite="infiniteHandler"
              spinner="waveDots"
            ></infinite-loading> -->
            <tr style="text-align: right; border-top: 1px solid #b0b0b0">
              <td class="pay" colspan="6" style="padding: 30px">
                <h5 style="display: inline-block; margin-right: 10px">
                  총 결제금액 :
                </h5>
                <h5 style="display: inline-block">
                  {{ total.toLocaleString() }} 원
                </h5>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="pay">
        <a class="primary-btn pd-cart nav-cart" @click="openModal">결제하기</a>
        <MyModal @close="closeModal" v-if="orderModal">
          <OrderForm
            :checkList="checkList"
            :total="total"
            @close="closeModal"
          />
        </MyModal>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MyModal from "../components/MyModal.vue";
import OrderForm from "./OrderForm.vue";
// import InfiniteLoading from "vue-infinite-loading";

export default {
  name: "Wishlist",
  components: {
    MyModal,
    OrderForm,
    // InfiniteLoading,
  },
  data() {
    return {
      orderModal: false,
      allChecked: false,
      check: [],
      liquor: "",
    };
  },

  methods: {
    openModal() {
      if (
        !this.$cookie.get("email") ||
        this.$cookie.get("email") != this.$store.state.email
      ) {
        this.$store.commit("logout");
        if (this.$cookie.get("name")) {
          this.$cookie.delete("name");
        }
        if (this.$cookie.get("email")) {
          this.$cookie.delete("email");
        }
        if (this.$cookie.get("userimg")) {
          this.$cookie.delete("userimg");
        }
        alert("세션이 만료되어 로그아웃되었습니다.");
        this.$router.push("/");
        return;
      }
      if (this.total == 0) {
        alert("상품을 선택해주세요!");
        return;
      }
      scrollTo(0, 0);
      this.orderModal = true;
    },
    closeModal() {
      this.orderModal = false;
    },
    checkAll() {
      this.check = [];
      if (!this.allChecked) {
        for (let index = 0; index < this.liquor.length; index++) {
          this.check.push(this.liquor[index].cart_id);
        }
      }
    },
    getLiquorList() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "cart/cartGet/" +
            this.$store.state.email
        )
        .then(({ data }) => {
          this.liquor = data;
        });
    },
    deleteLiquor(num) {
      axios
        .delete(process.env.VUE_APP_API_URL + "cart/cartUD/" + num)
        .then(({ data }) => {
          this.getLiquorList();
        });
    },
    // infiniteHandler($state) {
    //   if (this.liquor.length > this.limit) {
    //     axios
    //       .get(
    //         process.env.VUE_APP_API_URL +
    //           "cart/cartGet/" +
    //           this.liquor[this.limit].liquornumber
    //       )
    //       .then(({ data }) => {
    //         this.liquor[this.limit].review = data.length;
    //         axios
    //           .get(
    //             process.env.VUE_APP_API_URL +
    //               "cart/cartGet/" +
    //               this.liquor[this.limit].liquornumber
    //           )
    //           .then(({ data }) => {
    //             this.liquor[this.limit].score = Math.round(data.avg);
    //             this.products.push(this.liquor[this.limit]);
    //             $state.loaded(); // 계속 받는 상태로 둔다
    //             this.limit += 1;
    //           });
    //       });
    //   } else {
    //     $state.complete();
    //   }
    // },
  },
  created() {
    this.getLiquorList();
  },
  computed: {
    total() {
      let total = 0;
      for (let index = 0; index < this.liquor.length; index++) {
        if (this.check.indexOf(this.liquor[index].cart_id) != -1)
          total += this.liquor[index].liquorprice * this.liquor[index].quantity;
      }
      return total;
    },
    checkList() {
      return this.liquor.filter(
        (element) => this.check.indexOf(element.cart_id) != -1
      );
    },
  },
};
</script>

<style scoped lang="scss">
.primary-btn {
  float: right;
}
i {
  cursor: pointer;
}
input {
  text-align: center;
  transform: scale(2);
}

input:checked {
  background: #ffbbd6;
  border-color: #ffbbd6;
}
table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 1px 1px 7px #bbbbbb;
}
table th {
  font-size: 1rem;
  font-weight: 600;
  font-family: JSDongkang-Bold;
  vertical-align: middle;
  color: #3d4449;
  text-align: center;
  border-bottom: 1px solid #b0b0b0;
}
table tr {
  height: 3.5rem;
  text-align: center;
  padding: 1rem 0;
}

table td {
  vertical-align: baseline;
}

table tr td {
  padding: 1rem 0;
  font-size: 1rem;
}
@media (max-width: 500px) {
  table tr th:nth-child(2),
  td:nth-child(2) {
    display: none;
  }
}
button {
  text-align: center;
  justify-content: center;
}
.table-wrapper {
  word-break: break-all;
  -webkit-overflow-scrolling: touch;
  overflow-x: auto;
  word-break: break-all;
  font-size: 1em;
  padding-left: 7px;
  text-align: left;
  margin-top: 20px;
}

.btn-cover {
  margin-top: 1.5rem;
  text-align: center;
  cursor: default;
  vertical-align: middle;
}
.btn-cover .page-btn {
  height: 2rem;
  letter-spacing: 0.5px;
  text-align: left;
}
.btn-cover .page-count {
  padding: 0 1rem;
}
.product-list {
  padding: 0;
}
.pi-pic {
  width: 100px;
  height: 140px;
  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }
}
</style>