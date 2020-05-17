
import Vue from './vue.js'

import App from './App.js'

import './index.css'

new Vue({
   el:'#app',
   data(){
       return{

       }
   },
   template:
       `
       <div>
            <div>我是Vue实例对象</div>
            <App></App>
        </div>
       `,
    components:{
       App,
    }


});