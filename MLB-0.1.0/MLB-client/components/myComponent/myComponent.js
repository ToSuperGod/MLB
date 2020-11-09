var startPoint;
const min = 80;
const max = 294;
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    currentProgress: {
      type: Number,
      value: 0
    },
    maxProgress: {
      type: Number,
      value: 10
    },
    canSlide: {
      type: Boolean,
      value: true
    },
    progressName:{
      type:String,
      value:""
    },
    slideImg:{
      type:String,
      value:"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1714150507,3894444964&fm=26&gp=0.jpg"
    },
    titlesize:{
      type:String,
      value:"28rpx",
    },
    fontWeight:{
      type:Number,
      value:700,
    },
    color:{
      type: String,
      value: "#333333",
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    buttonLeft: 80,
    progress: 0,
    progressText: 0,
  },
  lifetimes: {
    attached: function() {
      // 在组件实例进入页面节点树时执行
      this.setData({
        progressText: (this.properties.currentProgress).toFixed(1),
        buttonLeft: this.properties.currentProgress * (max - min) / this.properties.maxProgress + min,
        progress: this.properties.currentProgress * (max - min) / this.properties.maxProgress
      })
    },
    detached: function() {
      // 在组件实例被从页面节点树移除时执行
    },
  },
  /**
   * 组件的方法列表
   */
  methods: {
    buttonStart: function(e) {
      startPoint = e.touches[0]
    },
    buttonMove: function(e) {
      if (!this.properties.canSlide) {
        return
      }
      var endPoint = e.touches[e.touches.length - 1]
      var translateX = endPoint.clientX - startPoint.clientX
      var translateY = endPoint.clientY - startPoint.clientY

      startPoint = endPoint;
      var buttonLeft = this.data.buttonLeft + translateX;
      if (buttonLeft > max) {
        return
      }
      if (buttonLeft < min) {
        return
      }
      //console.log(buttonLeft)
      this.setData({
        // buttonTop: buttonTop,
        buttonLeft: buttonLeft,
        progress: buttonLeft - min,
        progressText: ((buttonLeft - min) / (max - min) * this.properties.maxProgress).toFixed(1)
        //
      })
    },
    buttonEnd: function(e) {

    },

    /**
     * 获取分数
     */
    getScore(){
      return this.data.progressText
    },

    setCurrentProgress(progress){
      this.setData({
        currentProgress:progress,
        progressText: (progress).toFixed(1),
        buttonLeft: progress * (max - min) / this.properties.maxProgress + min,
        progress: progress * (max - min) / this.properties.maxProgress
      })
    }
  }
})