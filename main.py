import sublime, sublime_plugin
import boto3
from time import time

CLIENT = boto3.client('logs')

class CloudWatchLogsViewCommand(sublime_plugin.TextCommand):
    def run(self, edit, entity):
        sublime.set_timeout_async(lambda: self.load_events(entity), 0)


    def input(self, args):
        return EntityInputHandler()


    def load_events(self, entity):
        view = sublime.active_window().new_file()

        view.set_status('log_loading_indicator', 'retrieving log events...')
        view.set_scratch(True)
        view.set_name(entity)

        start = int((time() * 1000) - 60*60*1000)
        events = CLIENT.filter_log_events(logGroupName=entity, startTime=start, limit=100)

        while True:
            output = ""
            for event in (events['events']):
                output += "{msg}\n".format(msg = event['message'].strip())

            view.run_command("append", {"characters":output})

            if not 'nextToken' in events:
                break

            events = CLIENT.filter_log_events(logGroupName=entity, startTime=start, nextToken=events['nextToken'])

        view.erase_status('log_loading_indicator')
        sublime.status_message('Cloudwatch: logs loaded.')



class EntityInputHandler(sublime_plugin.ListInputHandler):
    def list_items(self):
      response = CLIENT.describe_log_groups()
      log_groups = []

      while True:
            for group in response['logGroups']:
                log_groups.append(group['logGroupName'])

            if not 'nextToken' in response:
                break

            response = CLIENT.describe_log_groups(nextToken=response['nextToken'])

      return log_groups


    def placeholder(self):
        return "Log Group"
