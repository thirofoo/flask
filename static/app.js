var info = document.getElementById('info')
var image = document.getElementById('image')

document.getElementById("get_image").onclick = () => {
  fetch("/image",{
    method: "GET",
  })
  .then(res => {
    console.log(res);
    if(res.ok)return res.text();
    else Promise.reject(new Error('エラーです。'));
  })
  .then(res => {
    var objRes = JSON.parse(res);
    console.log(objRes);
    Object.keys(objRes).forEach((key) => {
      info.innerHTML += "your " + key + " : " + objRes[key] + "<br>";
    })
    image.src = objRes['image'];
  })
}