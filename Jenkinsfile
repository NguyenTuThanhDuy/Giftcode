pipeline{
  agent any
  stages{
    stage('activate venv'){
      steps{
        sh '''
          cd ..
          cd Giftcode
          chmod 777 giftcode_env/Scripts/activate
          giftcode_env/Scripts/activate
        '''
      }
    }
    stage('check python version'){
      steps{
       sh 'python3 --version' 
      }
    }
    stage('check list components'){
      steps{
        sh 'pip list'
      }
    }
    stage('run giftcode'){
      steps{
        sh 'python3 giftcode.py'
      }
    }
  }
}
