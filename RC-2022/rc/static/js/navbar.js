
// var destination = new Date("Dec 15, 2021 00:00:00").getTime();
// var cont = setInterval(function() {
// var current = new Date().getTime();

// var diff = destination-current ;

// var hrs = Math.floor(diff%(24*60*60*1000)/(60*60*1000)) ;
// var mins = Math.floor(diff%(60*60*1000)/(60*1000)) ;
// var sec = Math.floor(diff%(60*1000)/(1000)) ;

// console.log(hrs)
// console.log(mins)
// console.log(sec)

// document.getElementById("timer").innerHTML = days + " : " + hrs + " : " + mins + " : " + sec
// document.getElementById("timer").style.borderTop = "thin solid #D3E0EA";

// },1000)

(function () {
  const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

  //I'm adding this section so I don't have to keep updating this pen every year :-)
  //remove this if you don't need it
  let today = new Date(),
    dd = String(today.getDate()).padStart(2, "0"),
    mm = String(today.getMonth() + 1).padStart(2, "0"),
    yyyy = today.getFullYear(),
    nextYear = yyyy + 1,
    dayMonth = "09/30/",
    birthday = dayMonth + yyyy;

  today = mm + "/" + dd + "/" + yyyy;
  if (today > birthday) {
    birthday = dayMonth + nextYear;
  }
  //end

  const countDown = new Date(birthday).getTime(),
    x = setInterval(function () {

      const now = new Date().getTime(),
        distance = countDown - now;

      //   document.getElementById("days").innerText = Math.floor(distance / (day)),
      document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);

      //do something later when date is reached
      if (distance < 0) {
        document.getElementById("headline").innerText = "";
        document.getElementById("countdown").style.display = "";
        document.getElementById("content").style.display = "";
        clearInterval(x);
      }
      //seconds
    }, 0)
}());