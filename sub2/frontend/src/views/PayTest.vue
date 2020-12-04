<template>
    <div>
        <button @click="pay">결제</button> <br/>
        <button @click="subsscription">구독</button> 
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Payment',
    data: () => ({
      dialog: false,
      items: [5000, 10000, 20000],
      value:''
    }),
    methods:{
        pay(){
            console.log("")
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            axios.post("http://127.0.0.1:8000/pay/index/")
            .then(res=>{
                let payUrl  = res.data.next_redirect_pc_url
                // console.log(res)
                this.$cookie.set("tid", res.data.tid, { expires: "1h" })
                location.href = payUrl
                
            })

        },
        subsscription(){
            console.log("")
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            axios.post("http://127.0.0.1:8000/pay/subscription/")
            .then(res=>{
                let payUrl  = res.data.next_redirect_pc_url
                    // console.log(res)
                    this.$cookie.set("subtid", res.data.tid, { expires: "1h" })
                    location.href = payUrl
            })    
        }
    }
}
</script>