$(function(){

  $('a').click(function(){
    if (document.getElementById('loading_modal')) {
      //prevent from running twice
      return true
    }
    var msg = this.getAttribute("loading");
    if (msg == null) { var msg = 'Please wait while loading...' };
    if($(this).attr('class') && $(this).attr('class').split(" ").indexOf("noloadingscreen") < 0) {
     $('<div class=loading_modal id="loading_modal"> \
     <div class="loading_innermodal">\
      <div class="sk-cube-grid">\
        <div class="sk-cube sk-cube1"></div>\
        <div class="sk-cube sk-cube2"></div>\
        <div class="sk-cube sk-cube3"></div>\
        <div class="sk-cube sk-cube4"></div>\
        <div class="sk-cube sk-cube5"></div>\
        <div class="sk-cube sk-cube6"></div>\
        <div class="sk-cube sk-cube7"></div>\
        <div class="sk-cube sk-cube8"></div>\
        <div class="sk-cube sk-cube9"></div>\
        </div>'+ msg +'\
      </div>\
      </div>').prependTo(document.body);

    }
 });

});
$(function(){
  $('button').click(function(){
    if (document.getElementById('loading_modal')) {
      //prevent from running twice
      return true
    }
    var msg = this.getAttribute("loading");
    if (msg == null) { var msg = 'Please wait while loading...' };
    if($(this).attr('class') && $(this).attr('class').split(" ").indexOf("noloadingscreen") < 0) {
     $('<div class=loading_modal id="loading_modal"> \
     <div class="loading_innermodal">\
      <div class="sk-cube-grid">\
        <div class="sk-cube sk-cube1"></div>\
        <div class="sk-cube sk-cube2"></div>\
        <div class="sk-cube sk-cube3"></div>\
        <div class="sk-cube sk-cube4"></div>\
        <div class="sk-cube sk-cube5"></div>\
        <div class="sk-cube sk-cube6"></div>\
        <div class="sk-cube sk-cube7"></div>\
        <div class="sk-cube sk-cube8"></div>\
        <div class="sk-cube sk-cube9"></div>\
        </div>'+ msg +'\
      </div>\
      </div>').prependTo(document.body);
    }
 });
});

function loading_modal(msg) {
  if (document.getElementById('loading_modal')) {
    //prevent from running twice
    return true
  }
  $('<div class=loading_modal id="loading_modal"> \
  <div class="loading_innermodal">\
   <div class="sk-cube-grid">\
     <div class="sk-cube sk-cube1"></div>\
     <div class="sk-cube sk-cube2"></div>\
     <div class="sk-cube sk-cube3"></div>\
     <div class="sk-cube sk-cube4"></div>\
     <div class="sk-cube sk-cube5"></div>\
     <div class="sk-cube sk-cube6"></div>\
     <div class="sk-cube sk-cube7"></div>\
     <div class="sk-cube sk-cube8"></div>\
     <div class="sk-cube sk-cube9"></div>\
     </div>'+ msg +'\
   </div>\
   </div>').prependTo(document.body);
};

function close_loading_modal() {
  var element = document.getElementById("loading_modal");
  if (element) {
    element.outerHTML = "";
    delete element;
  }

};
