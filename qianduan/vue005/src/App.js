import imgSrc from '../static/pic/meinv.jpg'

//定义一个组件
let App = {
    data(){
        return{
            img:imgSrc,
        }
    },
    template:
        `
            <div>
                我是App组件aaaaa
                <div>
                    <img :src="img" alt="">
                    <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554823994028&di=db5686fc98db2a66a0b4738645922f09&imgtype=0&src=http%3A%2F%2Fpic.feizl.com%2Fupload%2Fallimg%2F170614%2F1311511X7-2.jpg" alt="" width="200" height="200">
                </div>
            </div>
        `,
};

export default App;