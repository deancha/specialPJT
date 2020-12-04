<template>
  <div style="margin-top: 50px; margin-bottom: 50px">
    <div>
      <div class="product-list">
        <table class="product-item">
          <colgroup>
            <col width="4%" />
            <col width="7%" />
            <col width="20%" />
            <col width="7%" />
            <col width="3%" />
          </colgroup>
          <thead>
            <tr>
              <th>상품</th>
              <th>별점</th>
              <th>내용</th>
              <th>작성일</th>
              <th>삭제</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="!reviews || reviews.length == 0">
              <td colspan="5">남긴 리뷰가 없습니다.</td>
            </tr>
            <tr v-for="review in reviews" :key="review.review_id">
              <td>
                <div class="product-img">
                  <img
                    :src="'img/liquor/a' + review.liquornumber + '.jpg'"
                    alt="준비중"
                  />
                </div>
                {{ review.name }}
              </td>
              <td>
                <i class="fa fa-star" v-for="i in review.score"></i>
                <i class="fa fa-star-o" v-for="i in 5 - review.score"></i>
              </td>
              <td>{{ review.content }}</td>
              <td>
                {{ review.created_at.split("T")[0] }}
                {{ review.created_at.split("T")[1].substring(0, 5) }}
              </td>
              <td>
                <i
                  class="fa fa-remove"
                  @click="deleteReview(review.review_id)"
                ></i>
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
  name: "Reviewlist",
  data: () => ({
    reviews: [],
  }),
  computed: {},
  created() {
    this.getReviews();
  },
  methods: {
    getReviews() {
      this.reviews = [];
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "review/reviewbyuser/" +
            this.$store.state.email
        )
        .then(({ data }) => {
          data.forEach((element) => {
            axios
              .get(
                process.env.VUE_APP_API_URL + "liquor/" + element.liquornumber
              )
              .then(({ data }) => {
                element.img = data.url;
                element.name = data.liquorname;
                this.reviews.push(element);
              })
              .catch((data) => {
                this.deleteReview(element.review_id);
              });
          });
        });
    },
    deleteReview(id) {
      axios
        .delete(process.env.VUE_APP_API_URL + "review/" + id)
        .then((data) => {
          this.getReviews();
        });
    },
  },
};
</script>

<style lang="scss" scoped>
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
  /* background-color: #ffeced; */
}
table tr {
  height: 3.5rem;
  text-align: center;
  padding: 1rem 0;
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
.fa-remove {
  color: gray;
}
.fa-remove:hover {
  color: #b022b9;
  cursor: pointer;
}
@media (max-width: 500px) {
  table {
    thead {
      display: none;
    }
    td {
      display: block;
    }
    tr {
      border-bottom: 2px solid #cccccc;
    }

    img {
      max-width: 100px;
    }
  }
}
@media (min-width: 1264px) {
  .product-item {
    margin: 0 auto;
  }
}
.product-img {
  width: 100px;
  height: 100px;
  margin: 5px auto;
  img {
    object-fit: cover;
    width: 100%;
    height: 100%;
  }
}
</style>
