from motion_detector import df
from bokeh.models import HoverTool,ColumnDataSource   #columndatasource is the standardised way of providing data to a bokeh plot
from bokeh.plotting import figure,output_file,show

#formating time 
df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

#output file
output_file("Timeseries.html")

#create a figure object 
p=figure(plot_width=1000,plot_height=400,x_axis_type="datetime",title="Motion Graph")

hover = HoverTool(tooltips = [("Start","@Start_string"),("End","@End_string")])#@Satrt = df[Start],@End = df[End]
p.add_tools(hover)

p.quad(left="Start",right="End",top=1,bottom=0,source=cds)#providing data from cds - ColumnDataSource
show(p)
