import Vue from "vue";
import Router from "vue-router";

// 쇼핑몰
import Home from "../views/Home.vue";
import Detail from "../views/Detail.vue";
import Shop from "../views/Shop.vue";
import SubscriptionProduct from "../views/SubscriptionProduct.vue";

// 유저
import Login from "../views/Login.vue";

//에러
import PageNotFound from "../views/PageNotFound.vue";
import Error from "../views/Error.vue";

import Profile from "../views/Profile.vue";

//결제 테스트 페이지
import PayTest from "../views/PayTest.vue";
import PayCallBack from "../views/PayCallBack.vue";
import SubPayCallBack from "../views/SubPayCallBack.vue";

import Edu from "../views/Edu.vue";

// Routes
Vue.use(Router);

// Create a new router
const router = new Router({
  // mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/detail/:id",
      name: "Detail",
      component: Detail,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/shop",
      name: "Shop",
      component: Shop,
    },
    {
      path: "*",
      name: PageNotFound,
      component: PageNotFound,
    },
    {
      path: "/500/:msg",
      name: Error,
      component: Error,
    },
    {
      path: "/profile",
      name: "Profile",
      component: Profile,
    },
    {
      path: "/paytest",
      name: "PayTest",
      component: PayTest,
    },
    {
      path: "/pay",
      name: "PayCallBack",
      component: PayCallBack,
    },
    {
      path: "/edu",
      name: "Edu",
      component: Edu,
    },
    {
      path: "/subscription",
      name: "SubscriptionProduct",
      component: SubscriptionProduct,
    },
    {
      path: "/subpay",
      name: "SubPayCallBack",
      component: SubPayCallBack,
    },
  ],
});

export default router;
