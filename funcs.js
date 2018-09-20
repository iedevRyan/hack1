
        google.charts.load('current', {'packages':['table']});
        // google.charts.setOnLoadCallback(drawTable());



      function drawTable(tableData) {
        var data = new google.visualization.DataTable();
        data.addColumn('number', 'id');
        data.addColumn('string', 'Name');
        data.addColumn('number', 'Click Rate (%)');
        data.addColumn('number', 'App Tenure (%)');
        data.addColumn('number', 'Subscription Tenure (%)');
        data.addColumn('number', 'Loss (%)');
        // data.addColumn('boolean', 'Full Time Employee');
        data.addRows(tableData);

        var table = new google.visualization.Table(document.getElementById('table_div'));

        table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
      }

      function sendRequest() {
        var cur_cr_val = $("#cur_cr")[0].value;
        console.log("cur_cr_val: ", cur_cr_val);
        // alert(" cur_cr_val: " + cur_cr_val);
        var tar_cr = $("#tar_cr")[0].value;
        var notification_available = $("#notification_available")[0].value;

        jQuery.ajax("http://localhost:8088/data").done(function(data) {
          console.log("data:", drawTable(data))

        });


      }

      // [
      //     ['Mike',  {v: 10000, f: '$10,000'}, true],
      //     ['Jim',   {v:8000,   f: '$8,000'},  false],
      //     ['Alice', {v: 12500, f: '$12,500'}, true],
      //     ['Bob',   {v: 7000,  f: '$7,000'},  false]
      //   ]





//      <!--// test-->




// drawTable([
//           ['Mike',  {v: 10000, f: '$10,000'}, true],
//           ['Jim',   {v:8000,   f: '$8,000'},  false],
//           ['Alice', {v: 12500, f: '$12,500'}, true],
//           ['Bob',   {v: 7000,  f: '$7,000'},  false]
//         ]