"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        #'app/index.html',
        'app/home.html',
        context_instance = RequestContext(request,
        {
            'title':'User Log In',
            'year':datetime.now().year,
        })
    )

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


from app.forms import BootstrapCurveFittingForm
def T1LL_input(request):

    return render(
        request,
        'app/fitting_input.html',
        context_instance = RequestContext(request,
        {
            'title':'Fitting Input',
            'form': BootstrapCurveFittingForm
               })
    )


def T1LL_result(request):
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
    #return HttpResponse(y)

def highchart_hour():
    """original_data = ''
    for index in range(len(x)):
            if (index < (len(x) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (x[index], y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (x[index], y[index])
            original_data +=formattedline


    fitted_data = ''
    for index in range(len(fitted_y)):
            if (index < (len(fitted_y) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (smoothx[index], fitted_y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (smoothx[index], fitted_y[index])
            fitted_data += formattedline
"""
    JS="""
                <script type='text/javascript'>
                $(function () {
    $('#container').highcharts({
        title: {
            text: 'Hour'
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
            data: [3, 2, 1, 3, 4]
        }, {
            type: 'column',
            name: 'Female',
            color: '#f7a35c',
            data: [2, 3, 5, 7, 6]
        }, {
            type: 'pie',
            name: 'Total: ',
            data: [{
                name: 'Male',
                y: 13,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'Female',
                y: 23,
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
        <div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>



        """
    return JS

def highchart_day():
    """original_data = ''
    for index in range(len(x)):
            if (index < (len(x) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (x[index], y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (x[index], y[index])
            original_data +=formattedline


    fitted_data = ''
    for index in range(len(fitted_y)):
            if (index < (len(fitted_y) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (smoothx[index], fitted_y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (smoothx[index], fitted_y[index])
            fitted_data += formattedline
"""
    JS="""
                <script type='text/javascript'>
                $(function () {
    $('#container1').highcharts({
        title: {
            text: 'Day'
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
            data: [3, 2, 10, 3, 14]
        }, {
            type: 'column',
            name: 'Female',
            color: '#f7a35c',
            data: [2, 3, 5, 5, 6]
        }, {
            type: 'pie',
            name: 'Total: ',
            data: [{
                name: 'Male',
                y: 13,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'Female',
                y: 23,
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
        <div id="container1" style="min-width: 310px; height: 400px; margin: 0 auto"></div>



        """
    return JS

def highchart_month():
    """original_data = ''
    for index in range(len(x)):
            if (index < (len(x) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (x[index], y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (x[index], y[index])
            original_data +=formattedline


    fitted_data = ''
    for index in range(len(fitted_y)):
            if (index < (len(fitted_y) - 1)):
                formattedline = '				[%10.3f , %10.3f ],' % (smoothx[index], fitted_y[index])
            else:
                formattedline = '				[%10.3f , %10.3f ]' % (smoothx[index], fitted_y[index])
            fitted_data += formattedline
"""
    JS="""
                <script type='text/javascript'>
                $(function () {
    $('#container2').highcharts({
        title: {
            text: 'Month'
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
            data: [30, 42, 50, 34, 44]
        }, {
            type: 'column',
            name: 'Female',
            color: '#f7a35c',
            data: [42, 53, 45, 55, 46]
        }, {
            type: 'pie',
            name: 'Total: ',
            data: [{
                name: 'Male',
                y: 13,
                color: Highcharts.getOptions().colors[0] // Jane's color
            }, {
                name: 'Female',
                y: 23,
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
        <div id="container2" style="min-width: 310px; height: 400px; margin: 0 auto"></div>



        """
    return JS
