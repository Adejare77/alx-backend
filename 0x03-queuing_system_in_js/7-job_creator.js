const kue = require('kue');
const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

for (const job of jobs) {
  const queuedJob = queue.create('push_notification_code_2', job)
    .save((err) => {
      if (err) {
      // this error occurs during creation of the job
        console.error(`Notification job ${queuedJob.id} failed: ${err}`);
        return;
      }
      console.log(`Notification job created: ${queuedJob.id}`);
    });

  // Event listeners for each job completed, failed and progress
  queuedJob.on('complete', () => {
    console.log(`Notification job ${queuedJob.id} completed`);
  });

  // failed error occurs already created job fails during execution
  queuedJob.on('failed', (err) => {
    console.log(`Notification job ${queuedJob.id} failed: ${err}`);
  });

  // Reports on the progress of each job during execution not creation
  queuedJob.on('progress', (progress) => {
    console.log(`Notification job ${queuedJob.id} ${progress}% complete`);
  });
}
