var url = document.location.toString();
var arrUrl = url.split("//");
var good = arrUrl[1].split('/')[1];
console.log(url, arrUrl, good)
$.ajax({
    type: "get",
    url: "http://127.0.0.1:8000/v1/good/" + good + '/list',
    success: function(result) {
        if (200 == result.code) {
            for (var n = 0; n < result.data.length; n++)

            {
                document.getElementById('good_list').innerHTML += `<li><a href=""><div class="single_good" id="good_${n+1}"><img id="pic_${n+1}" src="" alt="" class="pic"><span id="title_${n+1}" class="title"></span><span id="time_${n+1}" class="time"></span><span id="price_${n+1}" class="price"></span></div></li>`
                document.getElementById(`pic_${n+1}`).src = 'http://127.0.0.1:8000/media/' + result.data[n].user + '/pic/' + result.data[n].pic
                document.getElementById(`title_${n+1}`).innerText = result.data[n].title + ' ' + result.data[n].content
                document.getElementById(`time_${n+1}`).innerText = result.data[n].time + '年 | TeamRay首发 | 到店服务 '
                document.getElementById(`price_${n+1}`).innerText = result.data[n].price + '元'
            }
            console.log('程序运行成功', result)
            console.log('result.data', result.data)
            console.log('result.data[0]', result.data[0])
            console.log('result.data[0].pic', result.data[0].pic)
        }
        if (201 == result.code) {
            document.getElementById('good_list').innerHTML += '<h1>没有找到任何商品</h1>'

        }
    }
})

console.log('这是我的js文件啦啦啦啦')


// document.getElementById('pic_1').src = 'http://127.0.0.1:8000/media/honey/pic/照片2.png'
// document.getElementById('title_1').innerText = '帅哥照片 ' + ' 本人毕业于北京吉利学院'
// document.getElementById('time_1').innerText = '2021' + '年 | TeamRay首发 | 到店服务 '
// document.getElementById('price_1').innerText = '9999.99' + '元'