// pages/menu/menu.js
Page({
  /**
   * 页面的初始数据
   */
  data: {
     camera:false,
     count:true,
     show:false,//控制预览图片显示
     show_1:false,//控制美化后图片显示
     src:"",//拍照临时图片地址
     base_1:"",//临时地址转化成的base64地址
     base1:"",//拍照后显示
     base_2:"",//后台传回来的base64地址
     base2:"", //接受api传送后显示
     index:0,
     num:0,//可拉进度条返回的数值
     Text:"",//添加的文字内容
     local_src:"",//背景图片临时地址
     base_local:"",//本地图片base64格式
     Functions:[
       {fun:"美白"},
       {fun:"复古"},
       {fun:"卡通画"},
       {fun:"铅笔画"},
       {fun:"北极寒"},
       {fun:"艾草绿"},
       {fun:"放大镜"},
       {fun:"素描"},
       {fun:"樱花"},
       {fun:"锐化"},
       {fun:"浮雕"},
       {fun:"调节色调"},  //需要参数 90~110
       {fun:"调节亮度"},   //需要参数 10~200
       {fun:"调节饱和度"},   //需要参数  5~100
       {fun:"添加文字"},  // 主传文字内容     辅传（可以不传）传文字颜色、大小、位置
       {fun:"瘦脸"},  //传参  10~250
       {fun:"蓝底证件照"},
       {fun:"红底证件照"},
       {fun:"更换背景"},  //传图片
       {fun:"超级美颜"},  
     ],//美颜功能
     order:0 //对应美颜功能对应的序号
  },
  login(){
    this.setData({
      camera:true,
      count:false,
      show:false,
      show_1:false
    })
  },
  takePhoto() { //调用相机拍照
    this.setData({
      show:true,
      base_2:""
    })
    const ctx = wx.createCameraContext()
    let that=this
    ctx.takePhoto({
      quality: 'high',
      success: (res) => {
        this.setData({
          src: res.tempImagePath,
          camera:false
        })
        console.log(this.data.src)
      }
    })
    setTimeout(function () {
      let src=that.data.src
      let base1=that.data.base1
      that.change_base64({
      url:src,
      type:'png'
    }).then(res=>{
      //console.log("转化成功")
      console.log(res)//res是base64路径
      base1="data:image/png;base64,"+res
      base1 = base1.replace(/[\r\n]/g, '') // 将回车换行换为空字符''
      that.setData({
        base_1:res,
        base1:base1
      })
      //console.log(that.data.base_1)
  })
     }, 1500) //延迟时间 这里是1.5秒
     setTimeout(function (){
      that.send_1()
     },3000)
  },

  change_base64({url,type}){
    return new Promise((resolve, reject) => {
      wx.getFileSystemManager().readFile({
        filePath: url, //选择图片返回的相对路径
        encoding: 'base64', //编码格式
        success: res => {
          resolve(res.data)  //'data:image/' + type.toLocaleLowerCase() + ';base64,' + 
          console.log("lalala")
        },
        //fail: res => reject(res.errMsg)
      })
      //console.log(res)
    })

  },

  get_1(){  //本地api获得数据
    let that=this
    let base2=this.data.base2
    wx.request({
      url: 'http://localhost:5000/my_send',  //服务器网址
      data: {
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        base2="data:image/png;base64,"+res.data
        base2 = base2.replace(/[\r\n]/g, '') // 将回车换行换为空字符''
        that.setData({
          base_2:res.data,
          base2:base2
        })
      }
    })
  },

  send_1(){ //向本地api传送照片
    let that=this
    let base_1=this.data.base_1
    wx.request({
      url: 'http://localhost:5000/my_get',  //服务器网址
      data: {
        base_1
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        console.log("success")
      }
    })
  },

  send_2(){ //向本地api传送功能序号
    let that=this
    //let order=this.data.order 
    let index=this.data.index
    let ondex=parseInt(index)+1
    console.log(ondex)
    wx.request({
      url: 'http://localhost:5000/my_signal',  //功能服务器网址
      data: {
        ondex
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        console.log("success")
      }
    })
  },

  send_4(){ //向本地api传送添加的文字
    let that=this
    let Text=this.data.Text
    console.log(Text)
    wx.request({
      url: 'http://localhost:5000/get_word',  //功能服务器网址
      data: {
        Text
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        console.log("success")
      }
    })
  },

  send_5(){ //向本地api传送背景图片地址
    let that=this
    let base_local=this.data.base_local
    wx.request({
      url: 'http://localhost:5000/other_image',  //功能服务器网址
      data: {
        base_local
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        console.log("success")
      }
    })
  },

  // send_3(){ //向本地api传送可拉进度条序号
  //   let that=this
  //   let num=this.data.num
  //   wx.request({
  //     url: 'http://localhost:5000/my_get',  //可拉进度条网址服务器网址
  //     data: {
  //       num
  //     },
  //     method: "POST",
  //     header: {
  //       'content-type': 'application/x-www-form-urlencoded',
  //       'chartset': 'utf-8'
  //     },
  //     success:function(res){
  //       console.log(res)
  //       console.log("success")
  //     }
  //   })
  // },

  beautiful(e){
    //console.log(e)
    let value=e.detail.value 
    this.setData({
      index:value,
      order:value+1
    })   //将功能数组角标赋值给index   0到n-1  
    this.myComponent = this.selectComponent("#myComponent");  
  },

   trans(){   //向后端传送数据，并接受数据，显示图片在小程序界面
      this.setData({
        base_2:"",
        show_1:true
      })
      let index=this.data.index
      let that=this
      this.send_2()   //传送功能序号
      if(index==14){
        this.send_4()
      }
      if(index==18){
        this.send_5()
      }
      // if(index==2){
      //   this.send_3()
      // }
      wx.showToast({
        title: '图片美化中...',
        icon: 'none',
        duration: 5000
      })
      setTimeout(function (){
         that.get_1()
      },5000)
      //两秒给后台处理图片，不够再加
   },

   getText(e){
     //属性值
    //console.log(e)
    let attr = e.target.dataset.set;
    // 值
    let value = e.detail.value;
    // console.log(attr)
    this.setData({
      [attr]:value
    })
   },

  getnum(){     //获得可拉进度条的返回值
    let index=this.data.index
    let num=this.data.num
   // console.log(this.myComponent.getScore())
    num=this.myComponent.getScore()
    console.log(parseInt(num))
    num=parseInt(num)+1    //num为1到10

    //判断为进度条的哪个功能
    if(index==11){  //90到110
      num=90+num*2
    }else if(index==12){   //10到200
      num=19*num
    }else if(index==13){  //5到100
      num=10*num
    }else if(index==15){   //10到250
      num=25*num
    }

    wx.request({
      url: 'http://localhost:5000/my_extent',  //可拉进度条网址服务器网址
      data: {
        num
      },
      method: "POST",
      header: {
        'content-type': 'application/x-www-form-urlencoded',
        'chartset': 'utf-8'
      },
      success:function(res){
        console.log(res)
        console.log("success")
      }
    })

    this.setData({
      num:num
    })
  },   

  back(){     //上传本地图片作为背景图
    let local_src=this.data.local_src
    let base_local=this.data.base_local
    let that=this
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],//图片尺寸：original:原图，compressed：压缩图
      sourceType: ['album', 'camera'],//图片来源：album：从相册选图，camera:使用相机
      success:(res)=> {
        console.log(res);
        local_src=res.tempFilePaths[0]
        that.change_base64({
          url:local_src,
          type:'png'
        }).then(res=>{
          //console.log("转化成功")
          console.log(res)//res是base64路径
          base_local=res
          that.setData({
            local_src:local_src,
            base_local:base_local
          })
          //console.log(that.data.base_1)
      })
      }
    })
  },

  Savelocal(){  //美化后图片保存至本地
    var imgSrc =  this.data.base_2;//美化后图片base64编码
    let src=this.data.src
    var save = wx.getFileSystemManager();
    var number = Math.random();
    save.writeFile({
      filePath: wx.env.USER_DATA_PATH + '/pic' + number + '.png',
      data: imgSrc,
      encoding: 'base64',
      success: res => {
        wx.saveImageToPhotosAlbum({
          filePath:wx.env.USER_DATA_PATH + '/pic' + number + '.png',
          success: function (res) {
            wx.showToast({
              title: '保存成功',
            })
          },
           fail: function (err) {
             console.log(err)
           }
        })
        console.log(res)
       }, fail: err => {
         console.log(err)
       }
    })
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    // this.myComponent = this.selectComponent("#myComponent");
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})
