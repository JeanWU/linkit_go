"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.decorators import login_required

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
        for row in cursor.fetchall()]

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        #'app/home.html',
        'app/try_0930.html',
        context_instance = RequestContext(request,{
            'title':'LinkitGo')       )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            #'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def showyoutube(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/youtube.html',
        {
            'title':'Youtube',
            'year':datetime.now().year,
        })

def showppt(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/ppt.html',
        {
            'title':'Presentation',
            'year':datetime.now().year,
        })


def dynamic_information(request):
    """Renders the dynamic_information page."""
    from django.db.models import Count
    from django.db import connection

    cursor = connection.cursor()
    sql_str3 = "select count(*) as sum1 from app_info_7688 where time1=datetime('now')"
    cursor.execute(sql_str3) #for superuser
    count_list = dictfetchall(cursor)
    count_now=count_list[0]['sum1']
    print("count_now=%d" %count_now)  #make sure that count_now is int and =0

    hi_try=highchart_try(count_now)

    assert isinstance(request, HttpRequest)
    result_dict={
        "highchart_try":hi_try
    }

    return render(
        request,
        'app/dynamic.html',
        context_instance = RequestContext(request, result_dict)       )





from django.contrib.auth.decorators import login_required
@login_required
def humanflow(request):
    """Renders the linkit_go page."""
    from django.db.models import Count
    from django.db import connection
    """retrun restaurant list
    :request: client request
    :returns: restaurant list webpage
    """
    cursor = connection.cursor()
    array0=[0,0,0,0,0]  #for male within hour
    array1=[0,0,0,0,0]  #for female within hour
    array2=[0,0,0,0,0]  #for male within day
    array3=[0,0,0,0,0]  #for female within day
    array4=[0,0,0,0,0]  #for male within month
    array5=[0,0,0,0,0]  #for female within month

    strlist=['10','20','30','40','50','60']
    for i in range (0,5,1):
        sql_str2 = "select count(case when time1 > datetime('now', '-1 hour') and age >= %s and age < %s then 1 else null end) as sum1 from app_info_7688 group by gender" %(strlist[i],strlist[i+1])
        cursor.execute(sql_str2) #for superuser
        summary = dictfetchall(cursor)
        array0[i]= summary[0]['sum1']
        array1[i]= summary[1]['sum1']

    for i in range (0,5,1):
        sql_str2 = "select count(case when time1 > datetime('now', '-1 day') and age >= %s and age < %s then 1 else null end) as sum1 from app_info_7688 group by gender" %(strlist[i],strlist[i+1])
        cursor.execute(sql_str2) #for superuser
        summary = dictfetchall(cursor)
        array2[i]= summary[0]['sum1']
        array3[i]= summary[1]['sum1']

    for i in range (0,5,1):
        sql_str2 = "select count(case when time1 > datetime('now', '-30 days') and age >= %s and age < %s then 1 else null end) as sum1 from app_info_7688 where time1 >= datetime('now','-1 month') group by gender" %(strlist[i],strlist[i+1])
        cursor.execute(sql_str2) #for superuser
        summary = dictfetchall(cursor)
        array4[i]= summary[0]['sum1']
        array5[i]= summary[1]['sum1']

    sql_str3 = "select count(*) as sum1 from app_info_7688 where time1=datetime('now')"
    cursor.execute(sql_str3) #for superuser
    count_list = dictfetchall(cursor)
    count_now=count_list[0]['sum1']


    hi_hour=highchart_hour(array0,array1,0)
    hi_day=highchart_hour(array2,array3,1)
    hi_month=highchart_hour(array4,array5,2)
    hi_try=highchart_try(count_now)

    assert isinstance(request, HttpRequest)
    result_dict={
        "highchart_hour":hi_hour,
        "highchart_day":hi_day,
        "highchart_month":hi_month,
        "highchart_try":hi_try
    }

    #add info into info_7688 table
    '''from .models import info_7688
    for i in range(10,60,5):
        info = info_7688(age='%d'%(i),gender=1,user_id=1)

        info.save()'''
    return render(
        request,
        #'app/index.html',
        'app/humanflow.html',
        context_instance = RequestContext(request, result_dict)       )
    #assert isinstance(request, HttpRequest)



def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'This is a website providing you the prediction of your property value.',
            'year':datetime.now().year,
        })
    )


"""from app.forms import BootstrapCurveFittingForm
def T1LL_input(request):

    return render(
        request,
        'app/fitting_input.html',
        context_instance = RequestContext(request,
        {
            'title':'Fitting Input',
            'form': BootstrapCurveFittingForm
               })
    )"""


"""def T1LL_result(request):
    #crime=request.POST.get('crime')
    hi_hour=highchart_hour()
    hi_day=highchart_day()
    hi_month=highchart_month()

    result_dict={
        "highchart_hour":hi_hour,
        "highchart_day":hi_day,
        "highchart_month":hi_month
    }
    return render(
    request,
    'app/boston_result.html',
    context_instance = RequestContext(request, result_dict)       )
    #return HttpResponse(y)"""

def highchart_hour(male=[3, 2, 1, 3, 10],female=[5,4,3,2,1],option=0):
    time_str=['hour','day','month']
    male_total=0
    for i in range(0,5,1):
        male_total+=male[i]
    female_total=0
    for i in range(0,5,1):
        female_total+=female[i]

    JS="""
                <script type='text/javascript'>
                $(function () {
    $('#$$container$$').highcharts({
        title: {
            text: '%s'
        },
        xAxis: {
            categories: ['10-20', '20-30', '30-40', '40-50', '50-60']
        },
        labels: {
            items: [{
                html: 'Total ',
                style: {
                    left: '50px',
                    top: '18px',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                }
            }]
        },
        series: [{
            type: 'column',
            name: 'Male',
            color: '#7cb5ec',
            data: %s
        }, {
            type: 'column',
            name: 'Female',
            color: '#f7a35c',
            data: %s
        }, {
            type: 'pie',
            name: 'Total: ',
            data: [{
                name: 'Male',
                y: %s,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'Female',
                y: %s,
                color: Highcharts.getOptions().colors[3] // John's color
            }],
            center: [100, 80],
            size: 100,
            showInLegend: false,
            dataLabels: {
                enabled: false
            }
        }]
    });
});

        </script>
        <div id="$$container$$" style="min-width: 310px; height: 400px; margin: 0 auto"></div>



        """ % (time_str[option],male,female,str(male_total),str(female_total))
    return JS.replace('$$container$$','container'+str(option))



def highchart_try(count_now):


    JS="""
                <script type='text/javascript'>
    $(function () {
    $(document).ready(function () {
        Highcharts.setOptions({
            global: {
                useUTC: false
            }
        });

        $('#container').highcharts({
            chart: {
                type: 'spline',
                animation: Highcharts.svg, // don't animate in old IE
                marginRight: 10,
                events: {
                    load: function () {

                        // set up the updating of the chart each second
                        var series = this.series[0];
                        setInterval(function () {
                            var x = (new Date()).getTime(), // current time
                                y = %s
                            series.addPoint([x, y], true, true);
                        }, 1000);
                    }
                }
            },
            title: {
                text: 'Live data'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        Highcharts.dateFormat('%%Y-%%m-%%d %%H:%%M:%%S', this.x) + '<br/>' +
                        Highcharts.numberFormat(this.y, 2);
                }
            },
            legend: {
                enabled: false
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'Random data',
                data: (function () {
                    // generate an array of random data
                    var data = [],
                        time = (new Date()).getTime(),
                        i;

                    for (i = -19; i <= 0; i += 1) {
                        data.push({
                            x: time + i * 1000,
                            y: %s
                        });
                    }
                    return data;
                }())
            }]
        });
    });
});

        </script>
        <div id="$$container$$" style="min-width: 310px; height: 400px; margin: 0 auto"></div>

        """ %(str(count_now),str(count_now))

    return JS.replace('$$container$$','container')
