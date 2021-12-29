def set_chart_option(dataFrame):
    titleList = list(dataFrame['name'].unique())
    
    chartOption = {
        "tooltip": {
        "trigger": "axis",
        "axisPointer": { "type": "shadow" }
      },
      "legend": {},
      "grid": { "left": "3%", "right": "4%", "bottom": "3%", "containLabel": True },
      "xAxis": { "type": "value", "name": "Sonic Video Games Sales in Millions", "nameLocation": "center", "nameGap": 30 },
      "yAxis": {
            "inverse": True,
            "type": "category",
            "data": titleList,
            "axisLabel": {
                "color": "#ffffff"    
            },
            "axisTick": {
                "show": False
            },
            "axisLine": {
                "lineStyle": {
                    "color": "#dedede"
                }
            }
      },
      "color": ['#fdc539','#6388fc','#ff6d70','#9c9899'],
      "series": [{
            "name": "North America",
            "type": "bar",
            "stack": "total",
            "label": {
                "show": True
            },
            "emphasis": {
                "focus": "series"
            },
            "data": list(dataFrame[dataFrame['region']=="North America"]['sales'])
        },
        {
            "name": "Europe Union",
            "type": "bar",
            "stack": "total",
            "label": {
                "show": True
            },
            "emphasis": {
                "focus": "series"
            },
            "data": list(dataFrame[dataFrame['region']=="Europe Union"]['sales'])
        },
        {
            "name": "Japan",
            "type": "bar",
            "stack": "total",
            "label": {
                "show": False
            },
            "emphasis": {
                "focus": "series"
            },
            "data": list(dataFrame[dataFrame['region']=="Japan"]['sales'])
        },
        {
            "name": "Other",
            "type": "bar",
            "stack": "total",
            "label": {
                "show": True
            },
            "emphasis": {
                "focus": "series"
            },
            "data": list(dataFrame[dataFrame['region']=="Other"]['sales'])
        }]
    }
    
    return chartOption