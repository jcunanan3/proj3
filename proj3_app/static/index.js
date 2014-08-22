$( document ).ready(function() {

//    The main opportunities to refactor are to store the category ids ('theft', 'robbery', etc.) as parameters in an array and then pass them to looped ajax calls in order to obtain the required data and then store that data in another array. I could then loop the highchart calls in another array. This would vastly reduce the amount of code in this file.

    console.log("ready!");
//    establish global variables to be passed between the ajax calls and the charting functions
    var crime_date=[];
    var assault_count=[];
    var assault_regression=[];
    var burglary_count=[];
    var burglary_regression=[];
    var theft_count=[];
    var theft_regression=[];
    var drugs_count=[];
    var drugs_regression=[];
    var robbery_count=[];
    var robbery_regression=[];
    var vehicletheft_count=[];
    var vehicletheft_regression=[];

//    call all of the ajax requests first

    // Could one call just return all of the information, 
    // especially if you're waiting for all of them to return anyways?
    $.when(
    $.when(
//        use a single date vector for all charts
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
            url: '/category_count/ASSAULT',
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
            url: '/category_count/'+'ROBBERY',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                robbery_count = response;
                console.log('robbery:',robbery_count);
            },
            error: function (response) {
                console.log(response)
            }
        }),
        $.ajax({
            url: '/category_count/'+'theft',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                theft_count = response;
                console.log('theft:',theft_count);
                console.log('#theft days:',theft_count.length)
            },
            error: function (response) {
                console.log(response)
            }
        }),
        $.ajax({
            url: '/category_count/'+'drugs',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                drugs_count = response;
                console.log('drugs:',drugs_count);
                console.log('#drug days:',drugs_count.length)
            },
            error: function (response) {
                console.log(response)
            }
        }),
        $.ajax({
            url: '/category_count/'+'BURGLARY',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                burglary_count = response;
                console.log('BURGLARY:',burglary_count);

            },
            error: function (response) {
                console.log(response)
            }
        }),

        $.ajax({
            url: '/category_count/'+'gta',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                vehicletheft_count = response;
                console.log('vehicle theft:',vehicletheft_count);

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
                assault_regression = response;
                console.log("regression: " + assault_regression);
            },
            error: function (response) {
                console.log(response)
            }
        }),
        $.ajax({
            url: '/cat_regression/' + 'BURGLARY',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                burglary_regression = response;
                console.log("burglary regression: " + burglary_regression);
            },
            error: function (response) {
                console.log(response)
            }
        }),

            $.ajax({
            url: '/cat_regression/'+'theft',
            type: 'GET',
            dataType: 'json',
            success: function (response) {
                theft_regression = response;
                console.log("theft regression: " + theft_regression);
            },
            error: function (response) {
                console.log(response)
            }
        }),
            $.ajax({
                url: '/cat_regression/'+'drugs',
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    drugs_regression = response;
                    console.log("drugs regression: " + drugs_regression);
                },
                error: function (response) {
                    console.log(response)
                }
            }),
            $.ajax({
                url: '/cat_regression/'+'ROBBERY',
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    robbery_regression = response;
                    console.log("robbery regression: " + robbery_regression);
                },
                error: function (response) {
                    console.log(response)
                }
            }),
            $.ajax({
                url: '/cat_regression/'+'gta',
                type: 'GET',
                dataType: 'json',
                success: function (response) {
                    vehicletheft_regression = response;
                    console.log("vehicle theft regression: " + vehicletheft_regression);
                },
                error: function (response) {
                    console.log(response)
                }
            })
//        all of the charting functions are called after the ajax data requests are fulfilled
    ).then(
        
        function() {
                // All of these highcharts are using mostly the same exact parameters.
                // You could make a function that makes the highchart with the default parameters
                // plus the couple of dynamic params.

//              console.log('highchart function ',crime_date, assault_count);
                $('#container').highcharts({
                    chart: {
                        type: 'line',
                        width: 1600
                    },
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
                        text: 'data.sfgov.org',
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
                            data: assault_regression
                        }
                    ]
                })}).then(
        function() {
                $('#container2').highcharts({
                    chart: {
                        type: 'line',
                        width: 1600
                    },
                    plotOptions:{
                        line: {
                            marker: {
                                radius: 1
                            }
                        }

                    },
                    title: {
                        text: 'Burglaries 2014',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'data.sfgov.org',
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
                            text: '# burglaries'
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
//
                        {
                            name:'burglary',
                            data: burglary_count
                        },
                        {
                            name:'regression',
                            data: burglary_regression
                        }
                    ]
                });
            }).then(

        function() {
                $('#container3').highcharts({
                    chart: {
                        type: 'line',
                        width: 1600
                    },
                    plotOptions:{
                        line: {
                            marker: {
                                radius: 1
                            }
                        }

                    },
                    title: {
                        text: 'Drugs 2014',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'data.sfgov.org',
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
                            text: '# drugs'
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
//
                        {
                            name:'drugs',
                            data: drugs_count
                        },
                        {
                            name:'regression',
                            data: drugs_regression
                        }
                    ]
                });
            }).then(


        function() {
                    $('#container4').highcharts({
                        chart: {
                        type: 'line',
                        width: 1600
                    },
                        plotOptions:{
                            line: {
                                marker: {
                                    radius: 1
                                }
                            }

                        },
                        title: {
                            text: 'Robbery 2014',
                            x: -20 //center
                        },
                        subtitle: {
                            text: 'data.sfgov.org',
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
                                text: '# robbery'
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
                                name:'robbery',
                                data: robbery_count
                            },
                            {
                                name:'regression',
                                data: robbery_regression
                            }
                        ]
                    });
                }).then(

        function() {
                $('#container5').highcharts({
                    chart: {
                        type: 'line',
                        width: 1600
                    },
                    plotOptions:{
                        line: {
                            marker: {
                                radius: 1
                            }
                        }

                    },
                    title: {
                        text: 'Vehicle Theft 2014',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'data.sfgov.org',
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
                            text: '# vehicle theft'
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
//
                        {
                            name:'vehicle theft',
                            data: vehicletheft_count
                        },
                        {
                            name:'regression',
                            data: vehicletheft_regression
                        }
                    ]
                });
            }).then(

            function() {
                $('#container6').highcharts({
                    chart: {
                        type: 'line',
                        width: 1600
                    },
                    plotOptions:{
                        line: {
                            marker: {
                                radius: 1
                            }
                        }

                    },
                    title: {
                        text: 'Theft 2014',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'data.sfgov.org',
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
                            text: '# thefts'
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
//
                        {
                            name:'theft',
                            data: theft_count
                        },
                        {
                            name:'regression',
                            data: theft_regression
                        }
                    ]
                });
            }
//    call the tabs functions last (very important!)
    )).done
        (
            function() {
                $( "#tabs" ).tabs();
              }
    )
    });
