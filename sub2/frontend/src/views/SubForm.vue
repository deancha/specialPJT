<template>
  <div
    style="
      padding: 10px;
      max-height: 620px;
      max-width: 1000px;
      position: relative;
      overflow-y: auto;
    "
  >
    <div style="text-align: right">
      <i @click="$emit('close')" class="fa fa-remove"></i>
    </div>
    <section class="checkout-section spad">
      <div class="container">
        <form class="checkout-form">
          <div class="row">
            <div class="col-lg-6">
              <div class="place-order">
                <h4>주문 내역</h4>
                <div class="order-total">
                  <ul class="order-table">
                    <li>
                      상품
                      <span>금액</span>
                    </li>
                    <li>
                      정기구독
                      <span>19,900 원</span>
                    </li>
                    <li class="total-price">
                      Total
                      <span> 19,900 원</span>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="col-lg-6">
              <div class="row">
                <div class="col-lg-12">
                  <label for="fir">
                    받는 사람
                    <span>*</span>
                  </label>
                  <input type="text" id="fir" v-model="name" />
                </div>

                <div class="col-lg-12">
                  <label for="street">
                    주소
                    <span>*</span>
                  </label>
                  <div class="col-lg-4" style="margin: 0; padding: 0">
                    <input
                      type="text"
                      placeholder="우편번호"
                      id="zipcode"
                      @click="getAddress"
                      readonly
                    />
                  </div>
                  <input
                    type="text"
                    id="street"
                    class="street-first"
                    placeholder="주소"
                    @click="getAddress"
                    readonly
                  />
                  <input
                    type="text"
                    placeholder="상세 주소"
                    v-model="addressDetail"
                  />
                </div>
                <div class="col-lg-12">
                  <label for="request">요청사항</label>
                  <input type="text" id="request" v-model="uniqueness" />
                </div>
                <div class="col-lg-12">
                  <label for="phone">
                    연락처
                    <span>*</span>
                  </label>
                  <input type="text" id="phone" v-model="phonenumber" />
                </div>
                <div class="col-lg-12" style="text-align: right">
                  <button class="primary-btn" type="button" @click="pay">
                    결제
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SubForm",
  components: {},
  data: () => ({
    addressDetail: "",
    uniqueness: "",
    phonenumber: "",
    totalQuantity: 0,
    ordername: "",
    modalAddress: false,
  }),
  computed: {
    zipcode() {
      return document.getElementById("zipcode").value;
    },
    address() {
      return document.getElementById("street").value;
    },
  },
  created() {
    this.list = this.$attrs.checkList;
    this.total = this.$attrs.total;
  },
  methods: {
    pay() {
      this.$cookie.set("kakaoemail", this.$store.state.email);
      this.$cookie.set("address", this.address + " " + this.addressDetail);
      this.$cookie.set("uniqueness", this.uniqueness);
      this.$cookie.set("phonenumber", this.phonenumber);
      this.$cookie.set("username", this.name);
      axios
        .post(process.env.VUE_APP_API_URL + "pay/subscription/")
        .then((res) => {
          let payUrl = res.data.next_redirect_pc_url;
          this.$cookie.set("subtid", res.data.tid, { expires: "1h" });
          this.$cookie.set("emails", this.$store.state.email);
          this.$cookie.set("address", this.address + this.addressDetail);
          location.href = payUrl;
        });
    },

    getAddress() {
      new daum.Postcode({
        oncomplete: function (data) {
          document.getElementById("street").value = data.address; // 도로명 주소 변수
          document.getElementById("zipcode").value = data.zonecode;
        },
      }).open();
    },
  },
};
</script>

<style lang="scss" scoped>
.checkout-form .place-order .order-total .order-table li {
  color: #252525;
  font-size: 15px;
  font-weight: 500;
}
.checkout-section {
  padding: 0px;
}
</style>
