# Import all the modules required
import subprocess
import sys
import time

def runCmd(command, cont=False, debug=False, log=None, **kwargs):
    ''' Run system commands (Supports both linux and Windows) '''

    # Create an empty return payload
    payload = {
        'result': None,
        'error': None,
        'status': False,
        'start_time': None,
        'end_time': None,
        'time': None,
        'cmd': str(command)
    }
    try:
        shell = False if type(command) == 'list' else True

        # Print the running command only if debug is True
        if debug: 
            print ("Running {}".format(payload['cmd']))

        # Capture the start time
        payload['start_time'] = time.time()

        # Run the command
        result = subprocess.Popen(command,
            shell=shell,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            cwd=kwargs['cwd'] if 'cwd' in kwargs.keys() else None,
            close_fds=kwargs['close_fds'] if 'close_fds' in kwargs.keys() else False
        )

        # Wait for the command to complete and cpature the output and error
        cmd_output, cmd_err = result.communicate()

        # Capture the end time
        payload['end_time'] = time.time()

        # Calculate the time taken for the command to complete
        payload['time'] = (payload['end_time'] - payload['start_time']) / 60

        # Write the Output and error to a log file
        if log:
            with open(log, "a+") as log_obj:
                log_obj.write(str(cmd_output))
                log_obj.write("\nError:\n{}".format(str(cmd_err)))
                log_obj.write("\nReturn Code: {}".format(result.returncode))
                log_obj.write("\nTime taken: {}\n".format(str(payload['time'])))

        # Get the result output of the command
        if result.returncode == 0:
            payload['result'] = cmd_output if cmd_output else None
            payload['status'] = True
        else: # Get the error output of the command
            payload['error'] = cmd_err if cmd_err  and 'Removing leading' not in cmd_err else None

    except subprocess.CalledProcessError as err:
        print ('Error: {}'.format(err))
        payload['error'] = str(err)
        if not cont:
            sys.exit(1)
    finally:
        return payload