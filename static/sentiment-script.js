$(document).ready(function(){
var positive = 0;
     var negative = 0;
     var neutral = 0;
 google.charts.load("current", {packages:["corechart"]});
 $('.searchText').click(function() {


  console.log("HEre")

  url = 'https://graph.facebook.com/USICT/?fields=id,name,posts{name,message},engagement,category';
    console.log(url);
  param = {
    "access_token": "EAACEdEose0cBAL8EZAs4YE7JqE5rFWd6Gp6wpR6AiDSazMiHdGASfCL0hiZCbUTRkYWMiXec9sxc6zkQAEaMZAv3vZCQS6qcVoA866toIQY1JNxlADZCSpTbphVSlZByC8sb4ZBcQGFqR3geb9LOSshQ2ezIu37Y9kc3OReHYXDqgZDZD"
  }

  $.getJSON(url, param, function(data){
    console.log(data);
     console.log(data.posts)

   // $('.results').html(JSON.stringify(data));

    data.posts.data.forEach(function(val){
    if(val.message!==undefined){
       $.ajax({
					url: "https://community-sentiment.p.mashape.com/text/",
					method: "POST",
					data: {
						txt: val.message
					},
					success: function(data) {
						console.log(data);
						if(data.result.sentiment=='Positive'){
							positive++;
							console.log("P" + positive);
						}
						else if(data.result.sentiment == 'Negative') {
							negative++;
							console.log("N" + negative);
						}
						else if(data.result.sentiment == 'Neutral') {
							neutral++;
							console.log("Neutral");
						}

					},
					error: function(err) {
						//console.log(err);
					},
					beforeSend: function(xhr) {
						xhr.setRequestHeader("X-Mashape-Authorization", "M53xm3Zeclmsh34NcEidLyPDgU6Pp1lsBdpjsnqmaNPfKZh1Hj");
					}
				})

    }

    });

    $('.showGraph').click(function(){
     drawChart();
    })
  });


     });
function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Sentiment Type', 'Percentage'],
          ['Postive',     positive],
          ['Neutral',      neutral],
          ['Negative',  negative]
        ]);

        var options = {
          title: 'SENTIMENT ANALYSIS OF FACEBOOK POSTS',
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
      }


});




