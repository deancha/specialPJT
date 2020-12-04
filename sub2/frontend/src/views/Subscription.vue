<template>
  <div style="margin-top: 50px; margin-bottom: 50px">
    <div>
      <div class="product-list">
        <table class="product-item">
          <thead>
            <tr>
              <th>주소</th>
              <th>결제 월수</th>
              <th>구독 취소</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="!sub || sub.length == 0">
              <td colspan="6">구독 내역이 없습니다.</td>
            </tr>
            <tr v-for="(s, i) in sub" :key="s.address">
              <td>{{ s.address }}</td>
              <td>{{ s.continuemonth }}개월</td>
              <td>
                <i class="fa fa-remove" @click="deleteSubscription"></i>
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
  name: "paginated-comment-list",
  data: () => ({
    sub: [],
  }),
  props: {},
  components: {},
  methods: {
    getSubscription() {
      axios
        .get(
          process.env.VUE_APP_API_URL +
            "subscription/" +
            this.$store.state.email
        )
        .then(({ data }) => {
          this.sub = data;
          console.log(data);
        });
    },
    deleteSubscription() {
      axios
        .delete(
          process.env.VUE_APP_API_URL +
            "subscription/" +
            this.$store.state.email
        )
        .then((data) => {
          console.log(data);
          alert("구독 취소 완료");
          this.getSubscription;
        });
    },
  },
  created() {
    this.getSubscription();
  },
  computed: {},
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
  padding: 10px;
}
</style>
