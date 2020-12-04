<template>
  <div>
    <MyModal @close="closeModal" v-if="orderModal">
      <SubForm @close="closeModal" />
    </MyModal>
    <div class="main">
      <div class="banner row">
        <div class="col-5">
          <div class="write">
            <h2>주당주당</h2>
            <h3>만의 서비스</h3>
            <h5>나에게 딱 맞는 전통주를 찾아보세요!</h5>
            <h5>전통주 정기 구독 서비스</h5>
            <h4>19,900원</h4>
          </div>
        </div>
        <div class="col-7 pic">
          <img src="@/assets/img/subsBanner.png" />
        </div>
      </div>
      <hr />
      <div class="row product">
        <div class="col-lg-7">
          <img src="@/assets/img/subscription.png" />
        </div>
        <div class="col-lg-5 write">
          <h3>
            <i class="fa fa-minus"></i>정기 구독 서비스<i
              class="fa fa-minus"
            ></i>
          </h3>
          <h5>지금 바로 구독 신청하세요</h5>
          <div class="part">
            <p>구성품</p>
            <p>추천 전통주 1병 ~ 2병</p>
            <p>스낵 안주</p>
          </div>
          <span>19,900원</span>
          <i class="fa fa-hand-o-right"></i>
          <button class="subs-btn" @click="openModal">구독하기</button>
        </div>
      </div>
      <hr />
      <div class="monthly">
        <h2>10월의 구성품</h2>
        <div class="row">
          <div class="col-lg-7">
            <img src="@/assets/img/10.png" />
          </div>
          <div class="col-lg-5 write">
            <h5>모든 전통주는 빅데이터를 기반으로</h5>
            <h5>본인에게 가장 알맞는 술을 넣어드립니다.</h5>
          </div>
        </div>
      </div>
      <hr />
      <div class="footer col-lg-11 row" style="margin: 0 auto">
        <div class="col-lg-4">
          <div class="col-9">
            <i class="fa fa-truck"></i>
            <p>
              주당주당이 직접 공수하여 유통을 최소화했습니다. 전통주를 빠른
              배송으로 신선하게 만날 수 있습니다.
            </p>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="col-9">
            <i class="fa fa-credit-card"></i>
            <p>
              세트 구성품으로 판매가보다 최소 15%부터 최대 25%까지 할인된
              합리적인 가격으로 받아보세요.
            </p>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="col-9">
            <i class="fa fa-heart"></i>
            <p>
              오직 본인에게 맞는! 전통주를 빅데이터를 활용하여 제공합니다.
              특색있는 전통주를 취향대로 만나보세요.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyModal from "../components/MyModal.vue";
import SubForm from "./SubForm.vue";
export default {
  components: {
    MyModal,
    SubForm,
  },
  data() {
    return {
      orderModal: false,
    };
  },
  created() {},

  methods: {
    openModal() {
      scrollTo(0, 0);
      if (!this.$store.state.email) {
        alert("로그인 후 이용가능한 서비스입니다.");
        return;
      }
      this.orderModal = true;
    },
    closeModal() {
      this.orderModal = false;
    },
  },
  computed: {},
};
</script>
<style lang="scss" scoped>
.main {
  text-align: center;
  padding: 30px 0;
  margin: 10px 20px 50px 20px;
  border-radius: 30px;
  background-color: #fff5f591;
  @media (max-width: 700px) {
    margin: 10px 5px 50px 5px;
  }
}
hr {
  width: 60%;
  margin: 5% auto;
  @media (max-width: 960px) {
    margin: 10% auto;
  }
}
.row {
  display: flex;
  align-items: center;
}
.subs-btn {
  display: inline-block;
  font-size: 17px;
  font-weight: 600;
  font-family: JSDongkang-Bold;
  padding: 15px 30px;
  border-radius: 10px;
  color: #ffffff;
  background: #ed8094;
  text-transform: uppercase;
  cursor: pointer;
}
.banner {
  display: flex;
  align-items: center;
  text-align: left;
  .write {
    padding-left: 30%;
    @media (max-width: 1070px) {
      padding-left: 20%;
    }
    h2 {
      display: inline-block;
      color: #e95c76;
      text-shadow: 4px 0px 3px #e2e1e1;
      margin-right: 5px;
    }
    h3 {
      display: inline-block;
      margin-bottom: 20px;
    }
    h4 {
      margin-top: 13px;
    }
  }
  .pic {
    text-align: left;
  }
  img {
    max-height: 300px;
    width: 80%;
    object-fit: cover;
  }
}
@media (max-width: 1263px) {
  .banner {
    img {
      max-height: 200px;
      width: 80%;
      object-fit: cover;
    }
  }
}
@media (max-width: 960px) {
  .banner {
    .write {
      padding-left: 20%;
      h2 {
        font-size: 20pt;
      }
      h3 {
        font-size: 16pt;
      }
      h4 {
        font-size: 15pt;
      }
      h5 {
        font-size: 12pt;
      }
    }

    img {
      max-height: 200px;
      width: 95%;
      object-fit: cover;
    }
  }
}
@media (max-width: 770px) {
  .banner {
    padding: 0 30px 0 30px;
    .write {
      padding-left: 0px;
    }
    img {
      max-height: 200px;
      width: 100%;
      object-fit: cover;
    }
  }
}
@media (max-width: 520px) {
  .banner {
    padding: 0 30px 0 30px;
    .write {
      padding-left: 0px;
      padding: 20px 0;
      h3 {
        display: none;
      }
    }
    img {
      max-height: 150px;
    }
  }
}
.product {
  img {
    max-height: 500px;
    padding-left: 5%;
    @media (max-width: 860px) {
      padding: 0;
    }
  }
  .write {
    @media (max-width: 860px) {
      padding: 0;
    }
    @media (min-width: 1300px) {
      padding-right: 20%;
    }
    h3 {
      margin-bottom: 10px;
      .fa-minus {
        margin: 0 7px;
        color: #adadad;
      }
    }
    h5 {
      margin-bottom: 2 0px;
    }
    .part {
      width: fit-content;
      padding: 10px;
      margin: 20px auto;
      border: 1px solid #e2e2e2;
      p {
        margin: 0px;
      }
    }
    span {
      font-family: "JSDongkang-Bold";
      font-size: 1.5rem;
      margin-right: 20px;
    }
    i {
      font-size: 1.5rem;
      margin-right: 20px;
    }
  }
}
.monthly {
  img {
    max-height: 300px;
  }
  h2 {
    text-align: left;
    padding-left: 15%;
    margin-bottom: 20px;
    @media (max-width: 700px) {
      font-size: 20pt;
      padding-left: 20px;
    }
  }
  .write {
    text-align: center;
    padding-right: 20%;
    @media (max-width: 1300px) {
      padding-right: 10%;
    }
    @media (max-width: 961px) {
      padding-right: 0px;
    }
    h5 {
      margin: 10px 0 0 0;
      color: grey;
    }
  }
}
.footer {
  > div {
    display: flex;
    justify-content: center;
  }
  i {
    font-size: 3rem;
    margin-bottom: 20px;
    color: #7cb5ef;
  }
}
</style>
