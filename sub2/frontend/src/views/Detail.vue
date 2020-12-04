<template>
  <div>
    <div class="row" id="check-out">
      <div class="col-8 check-out-form row">
        <div class="col-5 row info">
          <div class="pic">
            <img
              :src="'img/liquor/a' + $route.params.id + '.jpg'"
              alt="준비중"
            />
          </div>
          <div style="text-align: left; margin: auto 0; display: inline-block">
            <h5>{{ liquor.liquorname }}</h5>
            <p>{{ liquor.liquorprice.toLocaleString() }} 원</p>
          </div>
        </div>
        <div class="col-6 product-details" style="text-align: right">
          <div class="quantity" style="margin: 0">
            <div class="pro-qty">
              <span
                class="dec qtybtn"
                @click="
                  if (q2 > 1) {
                    q2 -= 1;
                  }
                "
                >-</span
              >
              <input type="text" v-model="q2" />
              <span class="inc qtybtn" @click="q2 += 1">+</span>
            </div>
            <button class="primary-btn pd-cart nav-cart" @click="addCart('q2')">
              Add To Cart
            </button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <section class="product-shop spad page-details">
        <div class="container">
          <div class="row">
            <!-- 상품 정보 -->
            <div
              class="col-lg-10"
              style="
                background-color: #ffecf47a;
                padding: 25px;
                border-radius: 30px;
                margin: 0 auto;
              "
            >
              <!-- 상품 헤더 -->
              <div class="row">
                <div class="col-lg-5">
                  <div class="product-pic-zoom">
                    <img
                      :src="'img/liquor/a' + $route.params.id + '.jpg'"
                      alt="준비중"
                    />
                    <div class="zoom-icon">
                      <i class="fa fa-search-plus"></i>
                    </div>
                  </div>
                </div>
                <div class="col-lg-7">
                  <div class="product-details">
                    <div class="pd-title">
                      <span>{{ liquor.liquorcategory }}</span>
                      <h3>{{ liquor.liquorname }}</h3>
                    </div>
                    <div class="pd-desc">
                      <p>
                        2019년 최고의 술, 대통령상을 받은 약주 #담백 #구수함
                        #바닐라향
                      </p>
                    </div>
                    <hr />
                    <div>
                      <p>도수 : {{ liquor.liquoralcohol }}%</p>
                      <p>용량 : 750mL</p>
                      <p>원료 : {{ liquor.liquoringredient }}</p>
                    </div>
                    <hr />
                    <div class="pd-rating">
                      <i class="fa fa-star" v-for="i in score"></i>
                      <i class="fa fa-star-o" v-for="i in 5 - score"></i>
                      <span>({{ totalReviews.length }})</span>
                    </div>
                    <div class="price">
                      <h4>{{ liquor.liquorprice.toLocaleString() }} 원</h4>
                    </div>
                    <div class="quantity">
                      <div class="pro-qty">
                        <span
                          class="dec qtybtn"
                          @click="
                            if (q1 > 1) {
                              q1 -= 1;
                            }
                          "
                          >-</span
                        >
                        <input type="text" v-model="q1" />
                        <span class="inc qtybtn" @click="q1 += 1">+</span>
                      </div>
                      <button
                        class="primary-btn pd-cart"
                        @click="addCart('q1')"
                      >
                        Add To Cart
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <div class="product-tab">
                <div class="tab-item">
                  <ul class="nav" role="tablist">
                    <li>
                      <a
                        class="active"
                        data-toggle="tab"
                        href="#tab-1"
                        role="tab"
                        >상세정보</a
                      >
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab-2" role="tab">상품정보</a>
                    </li>
                    <li>
                      <a data-toggle="tab" href="#tab-3" role="tab"
                        >리뷰/후기</a
                      >
                    </li>
                  </ul>
                </div>
                <div class="tab-item-content">
                  <div class="tab-content">
                    <div
                      class="tab-pane fade-in active"
                      id="tab-1"
                      role="tabpanel"
                    >
                      <div class="product-content">
                        <div class="row">
                          <div class="col-lg-9" style="margin: 0 auto">
                            <img
                              :src="'img/caption/' + $route.params.id + '.jpg'"
                              alt="상세정보를 준비중입니다."
                            />
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="tab-pane fade" id="tab-2" role="tabpanel">
                      <div class="specification-table">
                        <table>
                          <tr>
                            <td class="p-catagory">식품유형</td>
                            <td>
                              <div class="pd-rating">탁주</div>
                            </td>
                          </tr>
                          <tr>
                            <td class="p-catagory">생산자</td>
                            <td>
                              <div class="p-price">장희</div>
                            </td>
                          </tr>
                          <tr>
                            <td class="p-catagory">유통기한</td>
                            <td>
                              <div class="cart-add">제조일로부터 60일</div>
                            </td>
                          </tr>
                          <tr>
                            <td class="p-catagory">용량</td>
                            <td>
                              <div class="p-stock">500mL</div>
                            </td>
                          </tr>
                          <tr>
                            <td class="p-catagory">원재료 및 함량</td>
                            <td>
                              <div class="p-weight">
                                찹살 33.3%(국내산), 맵쌀 8.3%(국내산), 누룩
                                4.2%(국내산)
                              </div>
                            </td>
                          </tr>
                        </table>
                      </div>
                    </div>
                    <div class="tab-pane fade" id="tab-3" role="tabpanel">
                      <div class="customer-review-option">
                        <h4>리뷰 {{ totalReviews.length }} 건</h4>
                        <div class="comment-option">
                          <div
                            class="co-item"
                            v-for="review in reviews"
                            :key="review.review_id"
                            style="position: relative"
                          >
                            <div
                              class="avatar-text"
                              :id="'review' + review.review_id"
                            >
                              <div
                                style="position: absolute; right: 20px"
                                v-if="$store.state.email == review.kakaoemail"
                              >
                                <i
                                  class="fa fa-edit"
                                  :id="'edit' + review.review_id"
                                  style="margin-right: 5px"
                                  @click="editReview(review.review_id)"
                                ></i>

                                <i
                                  class="fa fa-remove"
                                  :id="'remove' + review.review_id"
                                  @click="deleteReview(review.review_id)"
                                ></i>
                              </div>
                              <div class="at-rating">
                                <i
                                  class="fa fa-star"
                                  v-for="i in review.score"
                                ></i>
                                <i
                                  class="fa fa-star-o"
                                  v-for="i in 5 - review.score"
                                ></i>
                              </div>
                              <h5>
                                {{ review.kakaoemail.substring(0, 3) }}***
                              </h5>
                              <span>{{
                                review.created_at.substring(0, 10)
                              }}</span>
                              <div class="at-reply">
                                {{ review.content }}
                              </div>
                            </div>
                            <div
                              class="avatar-text"
                              :id="'update' + review.review_id"
                              style="display: none"
                            >
                              <div style="position: absolute; right: 20px">
                                <i
                                  class="fa fa-check"
                                  :id="'check' + review.review_id"
                                  style="margin-right: 5px"
                                  @click="updateReview(review.review_id)"
                                >
                                </i>
                                <i
                                  class="fa fa-remove"
                                  :id="'cancel' + review.review_id"
                                  @click="cancelReview(review.review_id)"
                                ></i>
                              </div>
                              <div class="at-rating">
                                <v-rating
                                  v-model="updateRating"
                                  hover
                                ></v-rating>
                              </div>
                              <textarea
                                style="
                                  border: 1px solid #ebebeb;
                                  width: 100%;
                                  border-radius: 5px;
                                  height: 80px;
                                "
                                maxlength="100"
                                v-model="updateContent"
                              />
                            </div>
                          </div>
                          <v-pagination
                            v-model="page"
                            :length="length"
                            prev-icon="mdi-menu-left"
                            next-icon="mdi-menu-right"
                            :total-visible="5"
                          ></v-pagination>
                        </div>
                        <div class="leave-comment" v-if="writeReview">
                          <h4>리뷰 작성</h4>
                          <form class="comment-form">
                            <div class="row">
                              <div class="col-lg-12">
                                <div class="rating">
                                  <h5 style="display: inline-block">별점 :</h5>
                                  <v-rating v-model="rating" hover></v-rating>
                                </div>
                              </div>
                              <div class="col-lg-12">
                                <textarea
                                  placeholder="Messages"
                                  maxlength="100"
                                  v-model="content"
                                ></textarea>
                                <button
                                  type="button"
                                  class="site-btn"
                                  @click="addReview"
                                >
                                  등록
                                </button>
                              </div>
                            </div>
                          </form>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-2">
              <div style="position: relative">
                <div
                  :class="[{ 'relative-liquor-fixed': fixed }, 'filter-widget']"
                >
                  <h4 class="fw-title">비슷한 전통주</h4>
                  <div class="recommend-product-list">
                    <div
                      class="product"
                      v-for="liquor in relativeLiquor"
                      :key="liquor.liquornumber"
                      @click="move(liquor.liquornumber)"
                    >
                      <div class="product-card">
                        <img
                          :src="'img/liquor/a' + liquor.liquornumber + '.jpg'"
                        />
                      </div>

                      <p>{{ liquor.liquorname }}</p>
                      <span>{{ liquor.liquorprice.toLocaleString() }}원</span>
                    </div>
                  </div>
                  <div class="recommend-product-part">
                    <div class="up" @click="change('up')">
                      <i class="fa fa-sort-up" />
                    </div>
                    <div
                      class="product"
                      v-for="liquor in partLiquor"
                      :key="liquor.liquornumber"
                      @click="move(liquor.liquornumber)"
                    >
                      <div class="product-card">
                        <img
                          :src="'img/liquor/a' + liquor.liquornumber + '.jpg'"
                        />
                      </div>

                      <p>{{ liquor.liquorname }}</p>
                      <span>{{ liquor.liquorprice.toLocaleString() }}원</span>
                    </div>

                    <div class="down" @click="change('down')">
                      <i class="fa fa-sort-down" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
    <button class="scroll" @click="scrollTop">
      <img src="@/assets/img/scrollTop.png" />
    </button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      scrollY: 0,
      timer: null,
      liquor: {
        liquoralcohol: "",
        liquorarea: "",
        liquorcategory: "",
        liquoringredient: "",
        liquorname: "",
        liquornumber: "",
        liquorprice: "",
        url: "",
      },
      q2: 1,
      q1: 1,
      rating: 0,
      content: "",
      totalReviews: [],
      score: 0,
      updateRating: 0,
      updateContent: "",
      page: 0,
      length: 1,
      relativeLiquor: [],
      relativePos: 0,
      partLiquor: [],
      writeReview: false,
      fixed: false,
    };
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
    this.scrollTop();
    this.getLiquorDetail();
    this.getReviewList();
    this.getAvgScore();
    this.getRelativeLiquor();
    if (this.$store.state.email) {
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
        return;
      }
      this.possibleWriteReview();
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
            if (this.scrollY > 340 && window.innerWidth > 1260) {
              this.fixed = true;
            } else if (this.scrollY > 700) {
              document.getElementById("check-out").style.display = "block";
              this.fixed = false;
            } else {
              document.getElementById("check-out").style.display = "none";
              this.fixed = false;
            }
            clearTimeout(this.timer);
            this.timer = null;
          }.bind(this),
          100
        );
      }
    },
    possibleWriteReview() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "order/" +
            this.$store.state.email +
            "/" +
            this.$route.params.id
        )
        .then(({ data }) => {
          if (data.length > 0) this.writeReview = true;
        });
    },
    move(num) {
      this.$router.push("/detail/" + num);
    },
    getRelativeLiquor() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "contentsbasedrecommendation/" +
            this.$route.params.id +
            "/"
        )
        .then(({ data }) => {
          this.relativeLiquor = data;
          this.partLiquor = data.slice(0, 2);
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
    getReviewList() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "review/reviewscore/" +
            this.$route.params.id
        )
        .then(({ data }) => {
          this.totalReviews = data;
          this.length = Math.ceil(data.length / 5);
          this.page = 1;
        });
    },
    deleteReview(id) {
      axios
        .delete(process.env.VUE_APP_API_URL + "review/" + id)
        .then(({ data }) => {
          this.getReviewList();
          this.getAvgScore();
        });
    },
    getAvgScore() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "review/reviewavg/" +
            this.$route.params.id
        )
        .then(({ data }) => {
          this.score = Math.round(data.avg);
        });
    },
    editReview(id) {
      let idx = this.reviews.map((x) => x.review_id).indexOf(id);
      this.updateRating = this.reviews[idx].score;
      this.updateContent = this.reviews[idx].content;
      document.getElementById("review" + id).style.display = "none";
      document.getElementById("update" + id).style.display = "block";
    },
    cancelReview(id) {
      document.getElementById("review" + id).style.display = "block";
      document.getElementById("update" + id).style.display = "none";
    },
    updateReview(id) {
      axios
        .put(process.env.VUE_APP_API_URL + "review/" + id, {
          liquornumber: this.$route.params.id,
          kakaoemail: this.$store.state.email,
          score: this.updateRating,
          content: this.updateContent,
        })
        .then(({ data }) => {
          this.cancelReview(id);
          this.getReviewList();
        });
    },
  },
  computed: {
    reviews() {
      return this.totalReviews.slice(
        (this.page - 1) * 5,
        this.page == length ? this.totalReviews.length : this.page * 5
      );
    },
  },
};
</script>
<style lang="scss" scoped>
.pro-q {
  width: 123px;
  height: 46px;
  border: 2px solid #ebebeb;
  padding: 0 15px;
  float: left;
  margin-right: 14px;
  input {
    text-align: center;
    width: 52px;
    font-size: 14px;
    font-weight: 700;
    border: none;
    color: #4c4c4c;
    line-height: 40px;
    float: left;
  }
}
#check-out {
  display: none;
  text-align: center;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100000;
  .check-out-form {
    background-color: white;
    border-radius: 0 0 10px 10px;
    border: 2px solid #fd9393;
    border-top: none;
    margin: 0 auto;
    height: 80px;
    * {
      margin: 0;
      padding: 0;
    }
    .pic {
      max-height: 60px;
      max-width: 60px;
      margin-right: 10px;
      display: inline-block;
      img {
        object-fit: cover;
        width: 100%;
        height: 100%;
      }
    }
    .quantity {
      text-align: right;
    }
    .product-details {
      position: relative;
      .quantity {
        position: absolute;
        right: 0;
        .pro-qty {
          width: 100px;
          height: 46px;
          border: 2px solid #ebebeb;
          padding: 0 8px;
          float: left;
          margin-right: 14px;
          input {
            text-align: center;
            width: 40px;
            font-size: 13px;
            font-weight: 700;
            border: none;
            color: #4c4c4c;
            line-height: 40px;
            float: left;
          }
        }
      }
      .quantity .primary-btn.pd-cart {
        padding: 12px 30px;
      }
    }
  }
}
.price {
  margin: 10px 0px 20px 0px;
}
.tab-item-content {
  width: 98%;
  margin: 0 auto;
}
.scroll {
  position: fixed;
  width: 60px;
  right: 50px;
  bottom: 40px;
}
@media (max-width: 900px) {
  .scroll {
    display: none;
  }
}
@media (max-width: 1000px) {
  .info {
    display: none;
  }
  .product-details {
    flex: 100%;
    max-width: 100% !important;
  }
  .check-out-form {
    max-width: 300px;
  }
  .nav-cart {
    font-size: 13px;
  }
}
.v-rating {
  max-width: 70%;
  white-space: nowrap;
  display: inline-block;
}
.filter-widget {
  padding: 12px;
  text-align: center;
  h4 {
    margin-bottom: 20px;
  }
  .recommend-product-list {
    display: none;
    @media (max-width: 1260px) {
      display: flex;
      flex-wrap: wrap;
      flex: 1 1 auto;
    }
  }
  .recommend-product-part {
    @media (max-width: 1260px) {
      display: none;
    }
  }

  .up,
  .down {
    font-size: 2rem;
    cursor: pointer;
    i:hover {
      color: lightgray;
    }
  }
  .product:hover {
    box-shadow: 2px 2px 6px #808080a6;
  }
  .product {
    border-radius: 20px;
    border: 2px solid grey;
    margin-bottom: 20px;
    overflow: hidden;
    text-align: center;
    cursor: pointer;
    @media (max-width: 1260px) {
      flex: 0 0 17%;
      max-width: 17%;
      margin-right: 20px;
    }
    @media (max-width: 960px) {
      flex: 0 0 30%;
      max-width: 30%;
      margin-right: 20px;
    }
    @media (max-width: 850px) {
      flex: 0 0 45%;
      max-width: 45%;
      margin-right: 10px;
    }
    .product-card {
      width: 100%;
      height: 200px;
      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }
    p {
      margin-bottom: 5px;
      font-size: 1rem;
    }
  }
}
.relative-liquor-fixed {
  position: fixed;
  top: 0;
  max-width: 200px;
}
</style>
