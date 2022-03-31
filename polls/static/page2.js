console.log("page2js");
function myFunction(id){
console.log(id);
$.ajax({
    url: 'http://127.0.0.1:8000/polls/graph/'+id,
    type: 'GET',
    dataType: 'json',
    success: function (data) {
    console.log(data.choices);

var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"];
  new Chart("myChart", {
  type: "pie",
  data: {
    labels: data.choices,
    datasets: [{
      backgroundColor: barColors,

      data: data.votes
    }]
  },
  options: {
    title: {
      display: true,

    }
  }
});

}
});
}