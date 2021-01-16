###Busy Dialog with 'Busy.', 'Busy..', 'Busy...' animation
With many thanks to alias Tu®tle on discord who did all the animation.

> This dialog pops up and on progress checks if a variable check 
> is True before cancelling the animation and dismissing the dialog.

*THE COUNT (cnt) VARIABLE IN THIS EXAMPLE IS JUST TO ILLUSTRATE THE CONCEPT OF DISMISSAL*

For real implementation with your own check use the following `progression` function in the example instead:
```
    def progression(self, *args):
        if self.check:
            args[1].text = "Finished"
            Animation.cancel_all(args[1], 'dots')
            App.get_running_app().root.busy_dialog.dismiss()
        elif self.timeout == 20:
            args[1].text = "Timed out"
            Animation.cancel_all(args[1], 'dots')
            App.get_running_app().root.busy_dialog.dismiss()
```