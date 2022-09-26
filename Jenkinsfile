pipeline{
  agent any
  stages{
    stage('install requirements'){
      steps{
        sh '''
          cd ..
          cd Giftcode
          pip3.10 install -r requirements.txt
        '''
      }
    }
    stage('check python version'){
      steps{
       sh 'python3.10 --version' 
      }
    }
    stage('check list components'){
      steps{
        sh 'pip3.10 list'
      }
    }
    stage('run giftcode'){
      steps{
        sh 'python3.10 giftcode.py'
      }
    }
  }
}
