<template>
  <div class="container">
    <v-tabs content-class="mt-3" fill fixed-tabs v-model="tab">
      <v-tab> 장바구니 </v-tab>
      <v-tab> 구매내역 </v-tab>
      <v-tab> 리뷰 </v-tab>
      <v-tab> 구독 </v-tab>
    </v-tabs>
    <div>
      <Wishlist v-if="tab == 0" />
      <OrderList v-if="tab == 1" />
      <Reviewlist v-if="tab == 2" />
      <Subscription v-if="tab == 3" />
    </div>
  </div>
</template>
<script>
import axios from "axios";

import Wishlist from "@/views/Wishlist.vue";
import OrderList from "@/views/OrderList.vue";
import Reviewlist from "@/views/Reviewlist.vue";
import Subscription from "@/views/Subscription.vue";
export default {
  components: {
    Wishlist,
    OrderList,
    Reviewlist,
    Subscription,
  },
  data() {
    return {
      tab: null,
    };
  },
  methods: {},
};
</script>

<style scoped>
input[type="password"],
select,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  margin: 0 0 0 50;
}

button.leave {
  background-color: none;
  outline: none;
  border: none;
  box-shadow: none;
}

button.leave:hover {
  background-color: none !important;
  outline: none;
  border: none;
  box-shadow: none;
}

/* button:focus {
  outline: none;
} */
.container {
  display: block;
  width: 100vw;
  /* align-items: center;
  justify-content: center; */
}

.card {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  width: 80%;
  padding: 20px;
  /* align-items: center;
  justify-content: center; */
  margin: 0 auto;
}

* {
  box-sizing: border-box;
}

.form-group {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  margin-top: 10px;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  margin: 0 0 0 50;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
  text-align: left;
}

.btn1 {
  padding: 6px 12px;
  font-size: 17px;
  font-weight: normal;
  line-height: 1.428571429;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  cursor: pointer;
  border: 1px solid transparent;
  border-radius: 4px;
}

input[type="submit"] {
  justify-content: center;
}

input[type="submit"]:hover {
  background-color: #f67878;
}

.col-20 {
  float: left;
  width: 20%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 75%;
  margin-top: 6px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .col-25,
  .col-75,
  input[type="submit"] {
    width: 100%;
    margin-top: 0;
  }
}
</style>
