<template>
  <div>
    <!-- Hero Section Begin -->
    <section class="hero-section" style="margin-bottom: 30px">
      <div class="hero-items owl-carousel">
        <div class="single-hero-items set-bg" data-setbg="img/벚꽃.gif">
          <div class="container">
            <div class="row">
              <div
                class="col-lg-5"
                style="width: fit-content; background-color: #ffffff99"
              >
                <span>주당주당과 함께</span>
                <h1>전통주</h1>
                <p>주당주당과 함께 전통주의 새로운 세계를 즐겨보세요!</p>
                <router-link
                  to="/shop"
                  class="primary-btn"
                  style="background-color: #ed8094"
                  >Shop Now</router-link
                >
              </div>
            </div>
          </div>
        </div>
        <div class="single-hero-items set-bg" data-setbg="img/전통주배너.png">
          <div class="container" style="height: 250px"></div>
        </div>
      </div>
    </section>
    <!-- Hero Section End -->

    <!-- 주당주당 pick! Section Begin -->
    <section class="women-banner spad" v-if="bestLiquor.length != 0">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 offset-lg-1">
            <div class="filter-control">
              <h2>이번주에 가장 많이 팔린 전통주</h2>
            </div>
            <div class="product-slider owl-carousel">
              <div
                class="product-item"
                v-for="liquor in bestLiquor"
                :key="liquor.liquornumber"
                @click="move(liquor.liquornumber)"
              >
                <div class="pi-pic">
                  <img
                    :src="'img/liquor/a' + liquor.liquornumber + '.jpg'"
                    alt="준비중"
                  />
                </div>
                <div class="pi-text">
                  <h5>{{ liquor.liquorname }}</h5>
                  <div class="pd-rating">
                    <i class="fa fa-star" v-for="n in liquor.rate"></i>
                    <i class="fa fa-star-o" v-for="n in 5 - liquor.rate"></i>
                    <span>({{ liquor.review }})</span>
                  </div>
                  <div class="product-price">
                    {{ liquor.liquorprice.toLocaleString() }}원
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- 주당주당 pick! Section End -->
    <!-- 추천 알고리즘 Section Begin -->
    <section class="women-banner spad" v-if="recommendLiquor.length != 0">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 offset-lg-1">
            <div class="filter-control">
              <h2>나와 비슷한 사용자가 구매한 전통주</h2>
            </div>
            <div class="product-slider owl-carousel">
              <div
                class="product-item"
                v-for="liquor in recommendLiquor"
                :key="liquor.liquornumber"
                @click="move(liquor.liquornumber)"
              >
                <div class="pi-pic">
                  <img
                    :src="'img/liquor/a' + liquor.liquornumber + '.jpg'"
                    alt="준비중"
                  />
                </div>
                <div class="pi-text">
                  <h5>{{ liquor.liquorname }}</h5>
                  <div class="pd-rating">
                    <i class="fa fa-star" v-for="n in liquor.rate"></i>
                    <i class="fa fa-star-o" v-for="n in 5 - liquor.rate"></i>
                    <span>({{ liquor.review }})</span>
                  </div>
                  <div class="product-price">
                    {{ liquor.liquorprice.toLocaleString() }}원
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="women-banner spad" v-if="randomLiquor.length != 0">
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-8 offset-lg-1">
            <div class="filter-control">
              <h2>주당주당에서 추천하는 전통주</h2>
            </div>
            <div class="product-slider owl-carousel">
              <div
                class="product-item"
                v-for="liquor in randomLiquor"
                :key="liquor.liquornumber"
                @click="move(liquor.liquornumber)"
              >
                <div class="pi-pic">
                  <img
                    :src="'img/liquor/a' + liquor.liquornumber + '.jpg'"
                    alt="준비중"
                  />
                </div>
                <div class="pi-text">
                  <h5>{{ liquor.liquorname }}</h5>
                  <div class="pd-rating">
                    <i class="fa fa-star" v-for="n in liquor.rate"></i>
                    <i class="fa fa-star-o" v-for="n in 5 - liquor.rate"></i>
                    <span>({{ liquor.review }})</span>
                  </div>
                  <div class="product-price">
                    {{ liquor.liquorprice.toLocaleString() }}원
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="partner-logo" style="padding: 0 40px">
      <div class="row">
        <div class="col-4 logo" style="padding-top: 32px">
          <div style="margin: 0 auto; max-width: 150px">
            <img src="@/assets/img/logo.png" />
          </div>
        </div>
        <div class="col-2" style="padding-left: 20px">
          <div style="padding-top: 20px">
            <p>
              <strong style="font-family: 'JSDongkang-Bold'">팀장 </strong
              >차동우 (백엔드)
            </p>
            <p>서상원 (백엔드)</p>
            <p>신혜민 (프론트엔드)</p>
            <p>김수민 (프론트엔드)</p>
          </div>
        </div>
        <div class="col-2" style="padding-top: 32px; text-align: center">
          <p>
            <a
              href="https://www.notion.so/b452eec3ad7e4cbf868468165d1033f2"
              style="color: #636363"
            >
              <i
                class="fa fa-pencil"
                style="margin-right: 5px; font-size: 1.5rem"
              />Notion
            </a>
          </p>
          <p>
            <a
              href="https://lab.ssafy.com/s03-bigdata-sub3/s03p23a403"
              style="color: #636363"
            >
              <i
                class="fa fa-github"
                style="margin-right: 5px; font-size: 1.5rem"
              />GitHub
            </a>
          </p>
        </div>
        <div class="col-3" style="padding-top: 32px; text-align: center">
          <p>& SSAFY 3기 4반 3조</p>
          <p>ⓒ박선영없는박선영조</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      bestLiquor: [],
      recommendLiquor: [],
      randomLiquor: [],
    };
  },
  created() {
    this.getBestLiquor();
    if (this.$store.state.email) {
      this.getRecommendLiquor();
      this.getRandomLiquor();
    }
  },
  beforeDestroy: function () {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    scrollTop() {
      window.scrollTo(0, 0);
    },
    handleScroll: function () {
      if (this.timer === null) {
        this.timer = setTimeout(
          function () {
            this.scrollY = window.scrollY;
            if (this.scrollY > 700) {
              document.getElementById("check-out").style.display = "block";
            } else {
              document.getElementById("check-out").style.display = "none";
            }
            clearTimeout(this.timer);
            this.timer = null;
          }.bind(this),
          100
        );
      }
    },
    move(num) {
      this.$router.push("/detail/" + num);
    },
    getBestLiquor() {
      axios.get(process.env.VUE_APP_API_URL + "order/").then(({ data }) => {
        data.forEach((element) => {
          axios
            .get(
              process.env.VUE_APP_API_URL +
                "review/reviewscore/" +
                element.liquornumber
            )
            .then(({ data }) => {
              element.review = data.length;
              axios
                .get(
                  process.env.VUE_APP_API_URL +
                    "review/reviewavg/" +
                    element.liquornumber
                )
                .then(({ data }) => {
                  element.rate = Math.round(data.avg);
                  this.bestLiquor.push(element);
                  setTimeout(function () {
                    $.initialize();
                  }, 100);
                });
            });
        });
      });
    },
    getRandomLiquor() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "randomrecommendation/" +
            this.$store.state.email
        )
        .then(({ data }) => {
          data.forEach((element) => {
            axios
              .get(
                process.env.VUE_APP_API_URL +
                  "review/reviewscore/" +
                  element.liquornumber
              )
              .then(({ data }) => {
                element.review = data.length;
                axios
                  .get(
                    process.env.VUE_APP_API_URL +
                      "review/reviewavg/" +
                      element.liquornumber
                  )
                  .then(({ data }) => {
                    element.rate = Math.round(data.avg);
                    this.randomLiquor.push(element);
                    setTimeout(function () {
                      $.initialize();
                    }, 100);
                  });
              });
          });
        });
    },
    getRecommendLiquor() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "collaborativefilteringRecommendation/" +
            this.$store.state.email +
            "/"
        )
        .then(({ data }) => {
          data.forEach((element) => {
            axios
              .get(
                process.env.VUE_APP_API_URL +
                  "review/reviewscore/" +
                  element.liquornumber
              )
              .then(({ data }) => {
                element.review = data.length;
                axios
                  .get(
                    process.env.VUE_APP_API_URL +
                      "review/reviewavg/" +
                      element.liquornumber
                  )
                  .then(({ data }) => {
                    element.rate = Math.round(data.avg);
                    this.recommendLiquor.push(element);
                    setTimeout(function () {
                      $.initialize();
                    }, 100);
                  });
              });
          });
        });
    },
    change(mode) {
      if (mode == "up") {
        this.relativePos = this.relativePos == 0 ? 4 : this.relativePos - 1;
        this.partLiquor.pop();
        this.partLiquor.unshift(this.relativeLiquor[this.relativePos]);
      } else {
        this.relativePos = (this.relativePos + 1) % 5;
        this.partLiquor.shift();
        this.partLiquor.push(this.relativeLiquor[(this.relativePos + 1) % 5]);
      }
    },
    getLiquorDetail() {
      axios
        .get(process.env.VUE_APP_API_URL + "liquor/" + this.$route.params.id)
        .then(({ data }) => {
          this.liquor = data;
          setTimeout(function () {
            $.initialize();
          }, 100);
        });
    },
    addCart(num) {
      if (!this.$store.state.email) {
        alert("로그인 후 이용가능한 서비스입니다.");
        return;
      } else if (
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
        return;
      }
      axios
        .post(process.env.VUE_APP_API_URL + "cart/", {
          kakaoemail: this.$store.state.email,
          liquornumber: this.$route.params.id,
          liquorname: this.liquor.liquorname,
          liquorprice: this.liquor.liquorprice,
          url: this.liquor.url,
          quantity: num == "q1" ? this.q1 : this.q2,
        })
        .then(({ data }) => {
          if (confirm("장바구니에 담았습니다. 장바구니로 이동하시겠습니까?")) {
            this.$router.push("/profile");
          }
        });
    },
    addReview() {
      if (!this.$store.state.email) {
        alert("로그인 후 이용가능한 서비스입니다.");
        return;
      } else if (
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
        return;
      }
      if (this.content.length > 100) {
        alert("100자 이하로 작성해주세요.");
      } else {
        axios
          .post(process.env.VUE_APP_API_URL + "review/", {
            kakaoemail: this.$store.state.email,
            liquornumber: this.$route.params.id,
            score: this.rating,
            content: this.content,
          })
          .then(({ data }) => {
            alert("리뷰 작성 완료!");
            this.getReviewList();
            this.getAvgScore();
          });
      }
    },
  },
  computed: {},
};
</script>

<style scoped lang="scss">
.offset-lg-1 {
  margin: 0 auto;
}
.product-item:hover {
  box-shadow: 1px 1px 9px #ffb9c6;
}
.product-item {
  border-radius: 20px;
  box-shadow: 1px 1px 9px #c7c7c7;
  overflow: hidden;
  cursor: pointer;

  .fa {
    color: #e95c76;
  }
}
.pi-pic {
  height: 310px;
  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}
.product-price {
  margin-bottom: 10px;
}
</style>