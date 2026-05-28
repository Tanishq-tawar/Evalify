document.addEventListener("DOMContentLoaded", function () {

  function startCounter(id, target, speed) {
    let count = 0;
    let element = document.getElementById(id);

    if (!element) {
      console.error("Element not found:", id);
      return;
    }

    let interval = setInterval(() => {
      if (count < target) {
        count++;
        element.innerText = count;
      } else {
        clearInterval(interval);
      }
    }, speed);
  }

  startCounter("count1", 500, 5);
  startCounter("count2", 120, 20);
  startCounter("count3", 80, 30);

});
