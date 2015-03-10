/**
 * Created by gaoxiang on 15-3-7.
 * template and template render.
 */

var tpl = function(tpl,ArticleApi){
    var api="http://localhost:8000/api/Article/?format=json";
    this.ArticleApi=ArticleApi? ArticleApi:api,
    this.tpl=tpl
}

 //  JSON={title,content,timestap}
var template
//Rrender.
tpl.prototype.render=function(){

}

tpl.prototype.getArticle=function(){
    jsondata=$.get(this.ArticleApi);
    data = $.parseJSON(jsondata);
    return data;
}

/*
a=new tpl("<div></div>");
console.log(a.ArticleApi);*/
