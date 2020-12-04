<template>
  <div style="margin: 50px 0">
    <div>
      <div class="product-list">
        <table class="product-item">
          <thead>
            <tr>
              <th>주문 일자</th>
              <th>주문 번호</th>
              <th>주문 내역</th>
              <th>금액</th>
              <th>배달 상태</th>
              <th>삭제</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="!orderList || orderList.length == 0">
              <td colspan="6">주문 내역이 없습니다.</td>
            </tr>
            <tr v-for="(order, i) in orderList" :key="order.num">
              <td>
                {{ order.created_at.split("T")[0] }}
                {{ order.created_at.split("T")[1].substring(0, 5) }}
              </td>
              <td>{{ order.tid }}</td>
              <td><button @click="openModal(i)">보기</button></td>
              <td>{{ order.total.toLocaleString() }} 원</td>
              <td>
                <!-- 여기에 배송 조회 링크 걸어두기 -->
                <!-- <td @click="getDelivery(order.deliveryCode, order.deliveryNum)"> -->
                {{ order.status }}
              </td>
              <td><i class="fa fa-remove" @click="deleteOrder(i)"></i></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <MyModal @close="closeModal" v-if="orderModal">
      <OrderDetail
        v-if="isDetail"
        :detailOrder="detailOrder"
        :total="total"
        @close="closeModal"
      />
      <!-- <Delivery v-else @close="closeModal"></Delivery> -->
    </MyModal>
  </div>
</template>

<script>
import axios from "axios";
import MyModal from "../components/MyModal.vue";
import OrderDetail from "./OrderDetail.vue";

export default {
  name: "OrderList",
  components: {
    MyModal,
    OrderDetail,
  },
  data: () => ({
    orderModal: false,
    detailNum: 0,
    isDetail: false,
    totalList: [],
    orderList: [],
  }),
  computed: {
    detailOrder() {
      return this.totalList.filter(
        (element) => element.tid == this.orderList[this.detailNum].tid
      );
    },
    total() {
      return this.orderList[this.detailNum].total;
    },
  },
  created() {
    this.getOrderList();
  },
  methods: {
    openModal(pos) {
      this.detailNum = pos;
      this.isDetail = true;
      this.orderModal = true;
    },
    closeModal() {
      this.orderModal = false;
      this.isDetail = false;
    },
    getOrderList() {
      axios
        .get(
          process.env.VUE_APP_API_URL + "order/" + this.$store.state.email + "/"
        )
        .then(({ data }) => {
          this.totalList = data;
          this.orderList = [];
          let before = -1;
          for (let index = this.totalList.length - 1; index > -1; index--) {
            if (before != this.totalList[index].tid) {
              this.orderList.push(this.totalList[index]);
              this.orderList[this.orderList.length - 1].total =
                this.totalList[index].liquorprice *
                this.totalList[index].quantity;
              before = this.totalList[index].tid;
            } else {
              this.orderList[this.orderList.length - 1].total +=
                this.totalList[index].liquorprice *
                this.totalList[index].quantity;
            }
          }
        });
    },
    getDelivery(code, num) {
      window.open(
        "https://info.sweettracker.co.kr/api/v1/trackingInfo?t_key=Hld2ysA4YvlSjdCZKWY1zg&t_code=" +
          code +
          "&t_invoice=" +
          num
      );
    },
    deleteOrder(idx) {
      this.totalList
        .filter((list) => list.tid == this.orderList[idx].tid)
        .forEach((element) => {
          axios
            .delete(
              process.env.VUE_APP_API_URL +
                "order/" +
                this.$store.state.email +
                "/" +
                element.order_id
            )
            .then(({ data }) => {
              this.getOrderList();
            });
        });
    },
  },
};
</script>

<style scoped>
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
.fa-remove {
  color: gray;
}
.fa-remove:hover {
  color: #b022b9;
  cursor: pointer;
}
@media (max-width: 500px) {
  table tr th:nth-child(2),
  td:nth-child(2) {
    display: none;
  }
}
@media (min-width: 1264px) {
  .product-item {
    margin: 0 auto;
  }
}
</style>
