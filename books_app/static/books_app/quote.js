// function to load quotes.json
function loadJSON(callback) {
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', '/static/books_app/quotes.json', true); // Replace 'my_data' with the path to your file
  xobj.onreadystatechange = function () {
      if (xobj.readyState == 4 && xobj.status == "200") {
      // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
      callback(xobj.responseText);
      }
  };
  xobj.send(null);
}

// loading the quotes.json file
loadJSON(function(response) {
  var data = JSON.parse(response);
  appendData(data);
});

// function to create the necessary tags and send the data
// it picks out one quote for each day
function appendData(data) {
  var quoteContainer = document.getElementById("quote-data");
  var authorContainer = document.getElementById("quote-author");
  for (var i = 0; i < data.length; i++) {
    var today = new Date();
    var date = today.getDate();
    if(i+1 == date) {
      var em = document.createElement("em");
      var p = document.createElement("p");
      em.innerHTML = data[i].quote;
      p.innerHTML = '―' + data[i].author;
      quoteContainer.appendChild(em);
      authorContainer.appendChild(p);
    }
  }
}
