<template>
  <div>
    <header class="header-section">
      <div class="container">
        <div class="inner-header">
          <div class="row">
            <div class="logo">
              <a href="/">
                <img src="@/assets/img/logo.jpg" alt="logo" />
              </a>
            </div>
          </div>
          <div class="login" v-if="!$store.state.email" @click="login">
            <img src="@/assets/img/kakaoLogin.png" height="20px" />
            카카오로 로그인
          </div>
          <div class="login" v-if="$store.state.email">
            <div class="img">
              <img
                v-if="$store.state.userimg"
                :src="$store.state.userimg"
                alt="프로필"
              />
              <img
                v-if="!$store.state.userimg"
                src="@/assets/img/profile.png"
                alt="프로필"
              />
            </div>
            <span>
              <router-link to="/profile"
                >{{ $store.state.name }} 님</router-link
              >
            </span>
            <router-link to="/profile"
              ><i
                class="fa fa-shopping-cart"
                style="font-size: 1.3rem; margin-right: 10px; color: black"
              ></i
            ></router-link>

            <i
              @click="logout"
              class="fa fa-sign-out"
              style="font-size: 1.3rem"
            />
          </div>
        </div>
      </div>
      <div class="nav-item" style="width: 100%">
        <div class="container">
          <div class="nav-depart">
            <div class="depart-btn">
              <i class="ti-menu"></i>
              <span>전통주 카테고리</span>
              <ul class="depart-hover">
                <li>
                  <router-link to="/shop?category=막걸리"
                    >탁주, 막걸리</router-link
                  >
                </li>
                <li>
                  <router-link to="/shop?category=약주">약주, 청주</router-link>
                </li>
                <li>
                  <router-link to="/shop?category=와인">와인</router-link>
                </li>
                <li>
                  <router-link to="/shop?category=증류주">증류주</router-link>
                </li>
              </ul>
            </div>
          </div>
          <nav class="nav-menu mobile-menu">
            <ul>
              <li>
                <router-link to="/edu">전통주란?</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'Shop' }">쇼핑몰</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'SubscriptionProduct' }"
                  >구독</router-link
                >
              </li>
              <!-- <li>
                <router-link to="/profile">프로필</router-link>
              </li> -->
            </ul>
          </nav>
          <div class="input-group">
            <input
              type="text"
              v-model="word"
              placeholder="검색어를 입력해주세요."
              @keydown.enter="search()"
            />
            <button type="button" @click="search()">
              <i class="ti-search"></i>
            </button>
          </div>
          <div id="mobile-menu-wrap"></div>
        </div>
      </div>
      <div
        class="nav-item"
        id="nav"
        style="width: 100%; z-index: 10000; display: none; top: 0"
      >
        <div class="container">
          <div class="nav-depart">
            <div class="depart-btn">
              <i class="ti-menu"></i>
              <span>전통주 카테고리</span>
              <ul class="depart-hover">
                <li>
                  <router-link to="/shop?category=막걸리"
                    >탁주, 막걸리</router-link
                  >
                </li>
                <li>
                  <router-link to="/shop?category=약주">약주, 청주</router-link>
                </li>
                <li>
                  <router-link to="/shop?category=와인">와인</router-link>
                </li>
                <li>
                  <router-link to="/shop?category=증류주">증류주</router-link>
                </li>
              </ul>
            </div>
          </div>
          <nav class="nav-menu">
            <ul>
              <li>
                <a href="/edu">전통주란?</a>
              </li>
              <li>
                <router-link :to="{ name: 'Shop' }">쇼핑몰</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'SubscriptionProduct' }"
                  >구독</router-link
                >
              </li>
              <!-- <li>
                <router-link to="/profile">프로필</router-link>
              </li> -->
            </ul>
          </nav>
          <div class="input-group">
            <input
              type="text"
              v-model="word"
              placeholder="검색어를 입력해주세요."
              @keydown.enter="search"
            />
            <button type="button" @click="search">
              <i class="ti-search"></i>
            </button>
          </div>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      scrollY: 0,
      timer: null,
      word: "",
    };
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  beforeDestroy: function () {
    window.removeEventListener("scroll", this.handleScroll);
  },
  methods: {
    login() {
      window.location.href =
        process.env.VUE_APP_API_URL + "account/login/kakao/";
    },
    logout() {
      this.$store.commit("logout");
      // 쿠키 만료
      if (this.$cookie.get("name")) {
        this.$cookie.delete("name");
      }
      if (this.$cookie.get("email")) {
        this.$cookie.delete("email");
      }
      if (this.$cookie.get("userimg")) {
        this.$cookie.delete("userimg");
      }
    },
    handleScroll: function () {
      if (this.timer === null) {
        this.timer = setTimeout(
          function () {
            this.scrollY = window.scrollY;
            if (
              document.body.scrollWidth > 767 &&
              this.scrollY > 220 &&
              !document.URL.includes("/detail/")
            ) {
              document.getElementById("nav").style.display = "block";
              document.getElementById("nav").style.position = "fixed";
            } else {
              document.getElementById("nav").style.display = "none";
            }
            clearTimeout(this.timer);
            this.timer = null;
          }.bind(this),
          100
        );
      }
    },
    search() {
      this.$router.push("/shop?word=" + this.word);
    },
  },
};
</script>

<style lang="scss" scoped>
.logo {
  margin: 0 auto;
  img {
    height: 170px;
  }
}
.login {
  cursor: pointer;
  .img {
    display: inline-block;
    height: 25px;
    width: 25px;
    margin-right: 10px;
    border-radius: 20px;
    overflow: hidden;
    vertical-align: bottom;
    img {
      width: 25px;
      height: 25px;
      object-fit: cover;
    }
  }
  span a {
    color: grey;
    margin-right: 10px;
  }
}
@media only screen and (min-width: 768px) {
  .inner-header {
    position: relative;
    .login {
      position: absolute;
      right: 30px;
      top: 20px;
    }
  }
}
@media only screen and (max-width: 767px) {
  .login {
    position: relative;
    text-align: right;
    margin: 0 10px;
  }
}
.container {
  position: relative;
  .input-group {
    background-color: white;
    position: absolute;
    right: 20px;
    top: 15px;
    width: 25%;
    height: 40px;
    border-radius: 10px;
    padding: 5px;
    input {
      height: 100%;
      width: 90%;
    }
  }
}
</style>
