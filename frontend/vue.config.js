
module.exports = {
  // 部署应用包时的基本 URL
  // publicPath: process.env.NODE_ENV === 'production'
  //   ? '//your_url'
  //   : '/',

  // 运行 vue-cli-service build 时生成的生产环境构建文件的目录
  // 默认构建前清除文件夹(构建时传入 --no-clean 可关闭该行为
  outputDir: 'dist',

  // 放置生成的静态资源 (js、css、img、fonts) 的 (相对于 outputDir 的) 目录
  assetsDir: 'static',

  // 指定生成的 index.html 的输出路径 (相对于 outputDir),也可以是一个绝对路径
  indexPath: 'index.html',

  // 生成的静态资源在它们的文件名中包含了 hash 以便更好的控制缓存
  filenameHashing: true,

  // 当在 multi-page 模式下构建时，webpack 配置会包含不一样的插件
  // (这时会存在多个 html-webpack-plugin 和 preload-webpack-plugin 的实例)。
  // 如果你试图修改这些插件的选项，请确认运行 vue inspect
};
