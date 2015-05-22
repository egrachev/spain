var now = new Date();
var days = ['Воскресенье','Понедельник','Вторник','Среда',
    'Четверг','Пятница','Суббота'];
var months = ['Январь','Февраль','Март','Апрель','Май','Июнь',
    'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'];
var date = ((now.getDate()<10) ? "0" : "")+ now.getDate();

function four_digits(number)	{
	return (number < 1000) ? number + 1900 : number;
								}
today =  days[now.getDay()] + ", " +
         months[now.getMonth()] + " " +
         date + ", " +
         (four_digits(now.getYear())) ;


window.onload = function() {
    var el_time = document.getElementsByClassName('time');

    if (el_time.length > 0) {
        el_time[0].innerText = today;
    }
};
