<template>
  <div>
    <section class="product-shop spad">
      <div class="container">
        <div class="row">
          <div
            class="col-lg-3 col-md-6 col-sm-8 order-2 order-lg-1 produts-sidebar-filter"
          >
            <div class="filter-widget">
              <h4 class="fw-title">검색</h4>
              <div class="row" style="margin: 0">
                <input
                  v-model="word"
                  type="text"
                  class="search"
                  placeholder="검색어를 입력해주세요."
                  @keydown.enter="getFilter"
                />
                <button type="button" class="search-btn" @click="getFilter">
                  검색
                </button>
              </div>
            </div>
            <div class="filter-widget">
              <h4 class="fw-title">카테고리</h4>
              <div class="fw-tags">
                <input
                  type="checkbox"
                  v-model="filterCategory"
                  value="막걸리"
                  id="takju"
                />
                <label for="takju">탁주, 막걸리</label>
                <input
                  type="checkbox"
                  v-model="filterCategory"
                  value="약주"
                  id="yakju"
                />
                <label for="yakju">약주, 청주</label>
                <input
                  type="checkbox"
                  v-model="filterCategory"
                  value="와인"
                  id="wine"
                />
                <label for="wine">와인</label>
                <input
                  type="checkbox"
                  v-model="filterCategory"
                  value="증류주"
                  id="jeungnyu"
                />
                <label for="jeungnyu">증류주</label>
              </div>
            </div>

            <div class="filter-widget">
              <h4 class="fw-title">지역</h4>
              <div class="fw-brand-check">
                <div class="bc-item">
                  <label for="bc-GyeongGi">
                    경기도
                    <input
                      type="checkbox"
                      id="bc-GyeongGi"
                      v-model="filterArea"
                      value="경기도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="bc-item">
                  <label for="bc-ChungCheong">
                    충청도
                    <input
                      type="checkbox"
                      id="bc-ChungCheong"
                      v-model="filterArea"
                      value="충청도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="bc-item">
                  <label for="bc-GyeongSang">
                    경상도
                    <input
                      type="checkbox"
                      id="bc-GyeongSang"
                      v-model="filterArea"
                      value="경상도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="bc-item">
                  <label for="bc-Jeolla">
                    전라도
                    <input
                      type="checkbox"
                      id="bc-Jeolla"
                      v-model="filterArea"
                      value="전라도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="bc-item">
                  <label for="bc-GangWon">
                    강원도
                    <input
                      type="checkbox"
                      id="bc-GangWon"
                      v-model="filterArea"
                      value="강원도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
                <div class="bc-item">
                  <label for="bc-Jeju">
                    제주도
                    <input
                      type="checkbox"
                      id="bc-Jeju"
                      v-model="filterArea"
                      value="제주도"
                    />
                    <span class="checkmark"></span>
                  </label>
                </div>
              </div>
            </div>
            <div class="filter-widget">
              <h4 class="fw-title">가격</h4>
              <div class="filter-range-wrap">
                <div class="range-slider">
                  <div class="price-input">
                    <input type="text" id="minamount" />
                    <span style="margin: 0 10px; color: #ebebeb">ㅡ</span>
                    <input type="text" id="maxamount" />
                  </div>
                </div>
                <div
                  class="price-range ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content"
                  data-min="1000"
                  data-max="200000"
                >
                  <div
                    class="ui-slider-range ui-corner-all ui-widget-header"
                  ></div>
                  <span
                    tabindex="0"
                    class="ui-slider-handle ui-corner-all ui-state-default"
                  ></span>
                  <span
                    tabindex="0"
                    class="ui-slider-handle ui-corner-all ui-state-default"
                  ></span>
                </div>
              </div>
              <button class="filter-btn" @click="getFilter">Filter</button>
            </div>
            <div class="filter-widget">
              <h4 class="fw-title">리뷰 수</h4>
              <div class="fw-size-choose">
                <div class="sc-item">
                  <input
                    type="radio"
                    id="full"
                    v-model.number="filterCntReview"
                    value="0"
                  />
                  <label for="full">-</label>
                </div>
                <div class="sc-item">
                  <input
                    type="radio"
                    id="10"
                    v-model.number="filterCntReview"
                    value="10"
                  />
                  <label for="10">10+</label>
                </div>
                <div class="sc-item">
                  <input
                    type="radio"
                    id="20"
                    v-model.number="filterCntReview"
                    value="20"
                  />
                  <label for="20">20+</label>
                </div>
                <div class="sc-item">
                  <input
                    type="radio"
                    id="50"
                    v-model.number="filterCntReview"
                    value="50"
                  />
                  <label for="50">50+</label>
                </div>
              </div>
            </div>
          </div>

          <!-- 여기부터 상품 목록!!!!!!!!!!!!!!!!!!!!!!1 -->
          <div class="col-lg-9 order-1 order-lg-2 products-part">
            <div class="product-list">
              <div class="row">
                <div
                  class="col-lg-4 col-sm-6 col-xl-3 product-card"
                  v-for="product in products"
                  :key="product.liquornumber"
                  @click="mvDetail(product.liquornumber)"
                >
                  <div class="product-item">
                    <div class="pi-pic">
                      <img
                        :src="'/img/liquor/a' + product.liquornumber + '.jpg'"
                        alt="준비중"
                      />
                    </div>
                    <div class="pi-text">
                      <h5>{{ product.liquorname }}</h5>
                      <div class="pd-rating">
                        <i class="fa fa-star" v-for="i in product.score"></i>
                        <i
                          class="fa fa-star-o"
                          v-for="i in 5 - product.score"
                        ></i>

                        <span> ({{ product.review }}) </span>
                      </div>
                      <div class="product-price">
                        {{ product.liquorprice.toLocaleString() }}원
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <infinite-loading
              v-if="loading"
              :identifier="infiniteId"
              @infinite="infiniteHandler"
              spinner="waveDots"
            ></infinite-loading>
          </div>
        </div>
      </div>
    </section>
    <!-- Product Shop Section End -->
  </div>
</template>

<script>
import axios from "axios";
import InfiniteLoading from "vue-infinite-loading";

export default {
  components: {
    InfiniteLoading,
  },
  data: () => ({
    word: "",
    loading: false,
    infiniteId: 0,
    products: [],
    totalProducts: [],
    filterProducts: [],
    limit: 0,
    filterCntReview: 0,
    filterArea: [],
    filterCategory: [],
  }),
  computed: {},
  watch: {
    filterArea() {
      this.getFilter();
    },
    filterCategory() {
      this.getFilter();
    },
    filterCntReview() {
      this.products = [];
      this.limit = 0;
      this.infiniteId += 1;
    },
  },
  created() {
    if (this.$route.query.word) {
      this.word = this.$route.query.word;
    }
    if (this.$route.query.category) {
      this.filterCategory.push(this.$route.query.category);
    }
    this.getLiquor();
  },
  methods: {
    scrollTop() {
      window.scrollTo(0, 0);
    },
    mvDetail(num) {
      this.$router.push("/detail/" + num);
    },
    getLiquor() {
      axios.get(process.env.VUE_APP_API_URL + "liquor/").then(({ data }) => {
        this.totalProducts = data;
        this.loading = true;
        this.getFilter();
      });
    },
    getFilter() {
      this.filterProducts = this.totalProducts;
      if (this.word != "") {
        this.filterProducts = this.filterProducts.filter(
          (product) => product.liquorname.indexOf(this.word) != -1
        );
      }
      if (this.filterCategory.length != 0) {
        this.filterProducts = this.filterProducts.filter(
          (product) => this.filterCategory.indexOf(product.liquorcategory) != -1
        );
      }
      if (this.filterArea.length != 0) {
        this.filterProducts = this.filterProducts.filter(
          (product) => this.filterArea.indexOf(product.liquorarea) != -1
        );
      }
      let min = document
        .getElementById("minamount")
        .value.trim()
        .replace(/[^0-9]/g, "");
      let max = document
        .getElementById("maxamount")
        .value.trim()
        .replace(/[^0-9]/g, "");
      this.filterProducts = this.filterProducts.filter(
        (product) => min <= product.liquorprice && max >= product.liquorprice
      );
      this.products = [];
      this.limit = 0;
      this.infiniteId += 1;
    },
    // search() {},
    infiniteHandler($state) {
      if (this.filterProducts.length > this.limit) {
        axios
          .get(
            process.env.VUE_APP_API_URL +
              "review/reviewscore/" +
              this.filterProducts[this.limit].liquornumber
          )
          .then(({ data }) => {
            this.filterProducts[this.limit].review = data.length;
            axios
              .get(
                process.env.VUE_APP_API_URL +
                  "review/reviewavg/" +
                  this.filterProducts[this.limit].liquornumber
              )
              .then(({ data }) => {
                this.filterProducts[this.limit].score = Math.round(data.avg);
                // 여기서 한번더 평점 리뷰수, 가격이랑 일치하는지 체크
                if (
                  this.filterProducts[this.limit].review >= this.filterCntReview
                ) {
                  this.products.push(this.filterProducts[this.limit]);
                }
                $state.loaded(); // 계속 받는 상태로 둔다
                this.limit += 1;
              });
          });
      } else {
        $state.complete();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.offset-lg-1 {
  margin: 0 auto;
}
.products-part {
  background-color: rgba(255, 236, 244, 0.48);
  padding: 25px;
  border-radius: 30px;
}
.product-item {
  // border: 1px solid black;
  box-shadow: 3px 6px 11px 0px #ecd4dd;
  .pi-pic {
    height: 310px;
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }
  .pi-text {
    background-color: white;
    padding: 15px 0;
    h5 {
      margin-bottom: 5px;
    }
  }
}
.pd-rating * {
  color: #e95c76;
}
.search {
  border: 1px solid #ebebeb;
  padding: 8px;
  border-radius: 10px 0 0 10px;
}
.search-btn {
  background-color: #ffbbd6;
  color: white;
  padding: 8px;
  border-radius: 0 10px 10px 0;
}
.product-item:hover {
  cursor: pointer;
  margin: 5px;
}
.fw-tags label {
  cursor: pointer;
}
.fw-tags input[type="checkbox"] {
  display: none;
}
.fw-tags input:checked + label {
  background-color: grey;
  color: #ebebeb;
}
</style>
