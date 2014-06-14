$(function() {
  var imgList = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg'
  ], i = 0, $img = $('#img_slider'), imgPath = 'static/img/';

  function setSrc() {
    $img.attr('src', imgPath + imgList[i]);
    if (i < imgList.length - 1) {
      i++;
    }
    else {
      i = 0;
    }
    setTimeout(function() { setSrc(); }, 2000);
  }
  setSrc();
});