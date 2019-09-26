<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <!-- =========================================== -->
    <!-- PLEASE DO NOT EDIT ANYTHING ABOVE THIS LINE -->
    <!-- =========================================== -->

<div class="border border-secondary p-3 m-4">

<div class="alert alert-warning alert-dismissible fade show" role="alert">
  <strong>Warning:</strong> This web application is in active development. Don't use it until this message changes. 23 September 2019 
  <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>

<div class="card mb-3">
  <div class="card-header">
    Welcome
  </div>
  <div class="card-body">
    <h5 class="card-title">High School rotation maker</h5>
    <p class="card-text">This application helps to create rotating calendars for google calendar for the school year. This application only works for ASW. </p>
  </div>
</div>


<div class="row p-1 m-1">
    <div class="col-10">
            

        <form action="self_service_high_process.php" method="POST">

        <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter your school email">
            <small id="emailHelp" class="form-text text-muted">We'll never store or share your email.</small>
        </div>
<hr>



        <div class="form-group row">
            <label for="block_1" class="col-form-label">Block 1:</label>
            <div class="col-7">
                <input name="block_1" type="text" class="form-control" id="block_1" aria-describedby="block_help" placeholder="This text will appear for Block 1 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_2" class="col-form-label">Block 2:</label>
            <div class="col-7">
                <input name="block_2" type="text" class="form-control" id="block_2" aria-describedby="block_help" placeholder="This text will appear for Block 2 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_3" class="col-form-label">Block 3:</label>
            <div class="col-7">
                <input name="block_3" type="text" class="form-control" id="block_3" aria-describedby="block_help" placeholder="This text will appear for Block 3 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>


        <div class="form-group row">
            <label for="block_4" class="col-form-label">Block 4:</label>
            <div class="col-7">
                <input name="block_4" type="text" class="form-control" id="block_4" aria-describedby="block_help" placeholder="This text will appear for Block 4 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_5" class="col-form-label">Block 5:</label>
            <div class="col-7">
                <input name="block_5" type="text" class="form-control" id="block_5" aria-describedby="block_help" placeholder="This text will appear for Block 5 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>


        <div class="form-group row">
            <label for="block_6" class="col-form-label">Block 6:</label>
            <div class="col-7">
                <input name="block_6" type="text" class="form-control" id="block_6" aria-describedby="block_help" placeholder="This text will appear for Block 6 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_7" class="col-form-label">Block 7:</label>
            <div class="col-7">
                <input name="block_7" type="text" class="form-control" id="block_7" aria-describedby="block_help" placeholder="This text will appear for Block 7 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_8" class="col-form-label">Block 8:</label>
            <div class="col-7">
                <input name="block_8" type="text" class="form-control" id="block_8" aria-describedby="block_help" placeholder="This text will appear for Block 8 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>

        <div class="form-group row">
            <label for="block_9" class="col-form-label">Block 9:</label>
            <div class="col-7">
                <input name="block_9" type="text" class="form-control" id="block_9" aria-describedby="block_help" placeholder="This text will appear for Block 9 on your google calendar.">
                <small id="block_help" class="form-text text-muted">Keep it simple and short. No emoji's or line-breaks. If you keep this blank, nothing will appear on your calendar during this block.</small>
            </div>            
        </div>




        <button type="submit" class="btn btn-primary">Click to proceed to step 2</button>
        </form>

    </div>
</div>





</div> <!-- this closes the container div -->
    <!-- =========================================== -->
    <!-- PLEASE DO NOT EDIT ANYTHING BELOW THIS LINE -->
    <!-- =========================================== -->
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>
