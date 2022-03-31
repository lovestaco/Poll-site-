function myFun(item){
var val = document.querySelector('input[name="radivote"]:checked').value;
$.ajax({
            url: 'http://127.0.0.1:8000/polls/'+item.id+'/',
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify({ "incrementOption": val }),


        });
console.log("dfdsfn");
}