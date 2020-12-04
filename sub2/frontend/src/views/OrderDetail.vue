<template>
  <div
    class="orderDetail"
    style="
      padding: 10px;
      max-height: 620px;
      position: relative;
      overflow-y: auto;
    "
  >
    <div class="right">
      <i @click="$emit('close')" class="fa fa-remove"></i>
    </div>
    <div style="padding: 20px">
      <div class="product-list">
        <table class="product-item">
          <colgroup>
            <col width="200px" />
            <col width="300px" />
          </colgroup>
          <tbody>
            <tr class="head">
              <td class="left">
                <h5 style="font-size: 10pt">
                  {{ detailOrder[0].created_at.split("T")[0] }}
                  {{ detailOrder[0].created_at.split("T")[1].substring(0, 5) }}
                </h5>
              </td>
              <td class="right">
                <span style="font-size: 10pt"
                  >주문 번호 : {{ detailOrder[0].tid }}</span
                >
              </td>
            </tr>
            <tr class="lightHead">
              <td colspan="2" class="left">
                <h5>결제정보</h5>
              </td>
            </tr>
            <tr>
              <td>상품 가격</td>
              <td>{{ total.toLocaleString() }} 원</td>
            </tr>
            <tr class="lightHead">
              <td>배송비</td>
              <td>0 원</td>
            </tr>
            <tr class="head">
              <td><h5>총 금액</h5></td>
              <td>
                <h5>{{ total.toLocaleString() }} 원</h5>
              </td>
            </tr>
            <tr>
              <td colspan="2">
                <h5>{{ detailOrder[0].username }}</h5>
              </td>
            </tr>
            <tr class="lightHead">
              <td colspan="2">
                <div>{{ detailOrder[0].address }}</div>
                <p>{{ detailOrder[0].phonenumber }}</p>
              </td>
            </tr>
            <tr class="head">
              <td colspan="2">
                <p>{{ detailOrder[0].uniqueness }}</p>
              </td>
            </tr>
            <tr>
              <td colspan="2">
                <div>
                  <div
                    class="lightHead"
                    style="position: relative; padding-bottom: 10px"
                  >
                    <h5>
                      {{ detailOrder[0].status }}
                    </h5>
                    <!-- 여기에도 배송조회 링크 걸어두기 -->
                    <p style="position: absolute; top: 0; right: 5px">
                      배송 번호 : {{ detailOrder[0].waynumber }}
                    </p>
                  </div>
                  <div
                    class="row"
                    v-for="product in detailOrder"
                    :key="product.liquornumber"
                  >
                    <div class="col-3 p-img">
                      <img
                        :src="'img/liquor/a' + product.liquornumber + '.jpg'"
                        alt="준비중"
                      />
                    </div>
                    <div class="col-8">
                      <p>{{ product.liquorname }}</p>
                      <p>
                        {{ product.quantity }} 개 /
                        {{
                          (
                            product.liquorprice * product.quantity
                          ).toLocaleString()
                        }}
                        원
                      </p>
                    </div>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderDetail",
  components: {},
  data: () => ({
    detailOrder: null,
    total: null,
  }),
  computed: {},
  created() {
    // this.detailOrder = [];
    // this.getList();
    this.detailOrder = this.$attrs.detailOrder;
    this.total = this.$attrs.total;
  },
  methods: {
    getList() {
      this.$attrs.detailOrder.forEach((element) => {
        axios
          .get(process.env.VUE_APP_API_URL + "liquor/" + element.liquornumber)
          .then(({ data }) => {
            element.img = data.url;
            this.detailOrder.push(element);
          });
      });
    },
  },
};
</script>

<style lang="scss" scoped>
p {
  margin: 0;
  padding: 0;
}
table {
  max-width: 100%;
  border-collapse: collapse;
  border: 2px solid #ffbbd6;
  * {
    word-break: break-all;
  }
}
table tr:first-child {
  font-size: 1.1rem;
  font-weight: 600;
  font-family: JSDongkang-Bold;
  vertical-align: middle;
  color: #3d4449;
  text-align: left;
  background-color: #ffeced;
}
table tr {
  height: 3.5rem;
  text-align: left;
  padding: 1rem 0;
}
.head {
  border-bottom: 2px solid #ffbbd6;
}
.lightHead {
  border-bottom: 1px solid #ffe5ef;
}
table td {
  vertical-align: baseline;
  border-right: 1px solid #ffe5ef;
}

table tr td {
  padding: 1rem;
  font-size: 1.1rem;
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
  /* width: 5rem; */
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
.left {
  text-align: left;
}
.right {
  text-align: right;
}
.p-img {
  height: 120px;
  width: 120px;
  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }
}
.fa-remove {
  color: gray;
}
.fa-remove:hover {
  color: black;
  cursor: pointer;
}
</style>
