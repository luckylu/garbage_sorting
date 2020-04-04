<template>
<div class="layout">
  <Row type="flex" justify="center" style="margin-top: 80px">
    <Col>
      <picture>
  <source media="(max-width: 500px)" srcset="../assets/garbage1x.jpg">
  <source media="(min-width: 501px)" srcset="../assets/garbage.jpg">
  <img src="../assets/garbage1x.jpg" alt="cat">
</picture>
    </Col>
  </Row>
  <Row type="flex" justify="center" style="margin-top: 50px">
    <Col :xs="16" :md="6" :lg="6">
      <Input search enter-button size="large" v-model="garbage" @input="searchText" @on-search="clickResult(garbage)" placeholder="灵魂拷问：你是什么垃圾？" />
    </Col>
  </Row>
  <Row type="flex" justify="center">
    <Col :xs="16" :md="6" :lg="6">
      <List v-show="results.length > 0" class="results-list">
          <ListItem v-for="(item, index) in results" v-bind:key="index" @click.native="clickResult(item.name)">{{ item.name }}</ListItem>
      </List>
      </Col>
  </Row>
  <Row type="flex" justify="center" style="margin-top:20px" >
    <Col :xs="16" :md="6" :lg="6">
      <Card v-if="final_result !== ''">
        <p slot="title">{{final_result.category.name}}</p>
        <p v-show="final_result.category.id === 1">是指废纸张、废塑料、废玻璃制品、废金属、废织物等适宜回收、可循环利用的生活废弃物</p>
        <p v-show="final_result.category.id === 2">是指废电池、废灯管、废药品、废油漆及其容易等对人体健康或者自然环境造成直接或者潜在危害的生活废弃物</p>
        <p v-show="final_result.category.id === 4">即易腐垃圾，是指食材废料、剩菜剩饭、过期食品、瓜皮果核、花卉绿植、中药药渣等易腐的生物质生活废弃物</p>
        <p v-show="final_result.category.id === 8">即其他垃圾，是指除可回收物、有害垃圾、湿垃圾以外的其他生活废弃物</p>
      </Card>
      <Card v-show="no_result">
        <p><strong>这个垃圾尚未收录</strong></p>
      </Card>
    </Col>
  </Row>
</div>
</template>

<script>
function debounce(func, wait=200){ //可以放入项目中的公共方法中进行调用（鹅只是省事）
 let timeout;
 return function(event){
  clearTimeout(timeout)
  timeout = setTimeout(()=>{
   func.call(this, event)
  },wait)
 }
}

export default {
  name: 'Search',
  props: {
    msg: String
  },
  data: function(){
    return {
      garbage: '',
      results: [],
      no_result: false,
      final_result: ''
    }
  },
  methods: {
    searchText: debounce(function(){
      var that = this
      that.results = []
      that.no_result = false
      that.final_result = ''
      console.log(that.garbage)
      that.axios.get(process.env.VUE_APP_API_HOST+"/api/garbages/" + that.garbage + "/").then((response) => {
        if(response.data.length > 1){
          that.results = response.data
        }
      }).catch(function () {
        // handle error
        that.results = []
      })
    }),
    clickResult: function(name){
      var that = this
      that.garbage = name
      that.results = []
      that.no_result = false
      that.final_result = ''
      that.axios.get(process.env.VUE_APP_API_HOST+"/api/exact_garbages/" + name + "/").then((response) => {
        console.log(response.data)
        if(response.data.length === 1){
          that.final_result = response.data[0]
          that.no_result = false
          that.results = []
        }else if(response.data.length == 0){
          that.no_result = true
          that.final_result = ''
          that.results = []
        }else if(response.data.length > 1){
          that.final_result = ''
          that.no_result = false
          that.results = response.data
        }
      }).catch(function () {
        // handle error
          that.final_result = ''
          that.no_result = true
          that.results = []
      })
    }
  }
}
</script>

<style scoped>
.results-list{
  height: 300px;
  overflow-y: scroll;
  border: 0;
  border-radius: 0 0 24px 24px;
  box-shadow: 0 4px 6px 0 rgba(32,33,36,0.28);
}
.ivu-list-split .ivu-list-item {
    border-bottom: none;
    padding: 10px
}
.ivu-list-item:hover{
  background: #eee;
  background-origin: border-box;
}
</style>
