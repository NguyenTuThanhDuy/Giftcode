pipeline{
  agent any
  stages{
    stage('install requirements'){
      steps{
        sh '''
          cd ..
          cd Giftcode
          pip install -r requirements.txt
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
