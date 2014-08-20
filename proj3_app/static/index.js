$( document ).ready(function() {
    console.log("ready!");
    var crime_date=[];
    var assault_count=[];
    var regression=[];

    $.when(
        $.ajax({
            url: '/crime_date/',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                crime_date = response;
                console.log(crime_date);
            },
            error: function (response) {
                console.log(response)
            }
        }),

        $.ajax({
            url: '/assault_count/',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                assault_count = response;
                console.log(assault_count);
            },
            error: function (response) {
                console.log(response)
            }
        }),

        $.ajax({
            url: '/cat_regression/'+'ASSAULT',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                regression = response;
                console.log("regression: " + regression);
            },
            error: function (response) {
                console.log(response)
            }
        })
    ).done(
        function() {

              console.log('highchart function ',crime_date, assault_count);
                $('#container').highcharts({
                    plotOptions:{
                        line: {
                            marker: {
                                radius: 1
                            }
                        }

                    },
                    title: {
                        text: 'Assaults 2014',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'datasf.gov',
                        x: -20
                    },
                    xAxis: {
                        categories: crime_date,
                        labels:{
                            step: 20,
                            rotation: 30,
//                            maxStaggerLines:10,
                            tickPixelInterval: 100
                        }
                    },

                    yAxis: {
                        title: {
                            text: '# assaults'
                        },
                        plotLines: [
                            {
                                value: 0,
                                width: 1,
                                color: '#808080'
                            }
                        ]
                    },

                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle',
                        borderWidth: 0
                    },
                    series: [
                        {
                            name: 'assaults',
                            data: assault_count

                        },
                        {
                            name:'regression',
                            data: regression
                        }
                    ]
                });
            }

        );

    });
