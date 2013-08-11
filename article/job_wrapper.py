from article.models import Article, JobData
from WorkflowPrototype1.workflow.workflow_user import Workflow_user
from WorkflowPrototype1.workflow.workflow_setting import brokers
import json



class JobWrapper(object):

    def __init__(self):
        pass


    def readDB(self, jobID):
        """
        read data from django database
        pass jobID to obtain parameters
        """
        cur_obj = Article.objects.get(id=jobID)

        self.angle_start = int(cur_obj.angle_start)
        self.angle_end = int(cur_obj.angle_end)
        self.angle_step = int(cur_obj.angle_step)

        self.job = str(cur_obj.algorithm)
        self.username = "user1"
        self.passcode = "pw"
        self.title = str(cur_obj.title)
        self.file_p = "../static/images/"

        self.output_file = str(self.username)+"_"+str(self.title)+".jpeg"
        self.information = str(int(cur_obj.angle_start))+" "+str(int(cur_obj.angle_end))+" "+str(int(cur_obj.angle_step))

        self.tool_id = jobID

        return


    def run_job(self):
        """
        call ActiveMQ
        """
        message = {"instrument": "HXN",
            "job": self.job,
            "user": self.username,
            "passcode": self.passcode,
            "input_data_file": "filename.png",
            "output_data_file": self.file_p+self.output_file,
            "information": self.information,
            "method": ""
        }

        wu = Workflow_user(brokers, self.username, self.passcode)
        msg = json.dumps(message)
        wu.submit(msg)

        return


    def saveDB(self, tool_name):
        """
        save to new database
        """
        job_obj = JobData.objects.all()
        new_id = len(job_obj)+1
        print new_id

        newjob = JobData()

        newjob.job_id = new_id
        newjob.tool_name = tool_name
        newjob.tool_id = self.tool_id
        newjob.save()

        return



    def addDB(self, new_name):
        """
        add different tools into the job database
        same job ID
        """
        pass




def test():
    pass


if __name__=="__main__":
    test()


