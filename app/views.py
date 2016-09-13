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
    hi_hour=highchart_hour([1,2,3,4,5],[1,2,3,4,10],0)
    hi_day=highchart_hour([1,2,3,4,5],[1,2,3,4,1],1)
    hi_month=highchart_hour([1,2,3,4,5],[1,2,3,4,2],2)
    assert isinstance(request, HttpRequest)
    result_dict={
        "highchart_hour":hi_hour,
        "highchart_day":hi_day,
        "highchart_month":hi_month
    }

    from .models import PI_info
    info = PI_info(age=20,gender=1)

    info.save()
    return render(
        request,
        #'app/index.html',
        'app/humanflow.html',
        context_instance = RequestContext(request, result_dict)       )

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

def linkit_go(request):
    """Renders the linkit_go page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/linkit_go.html',
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
        <div id="$$container$$" style="min-width: 310px; height: 400px; margin: 0 auto"></div>



        """ % (time_str[option],male,female)
    return JS.replace('$$container$$','container'+str(option))
