<edu.wpi.grip.core.Pipeline>
  <sources>
    <edu.wpi.grip.core.sources.MultiImageFileSource>
      <property name="path[13]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190841.jpg"/>
      <property name="path[9]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190817.jpg"/>
      <property name="path[10]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190825.jpg"/>
      <property name="path[6]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190804.jpg"/>
      <property name="path[3]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190753.jpg"/>
      <property name="path[0]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190512.jpg"/>
      <property name="path[12]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190837.jpg"/>
      <property name="path[8]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190813.jpg"/>
      <property name="index" value="1"/>
      <property name="numImages" value="14"/>
      <property name="path[5]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190801.jpg"/>
      <property name="path[2]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190750.jpg"/>
      <property name="path[11]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190834.jpg"/>
      <property name="path[7]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190810.jpg"/>
      <property name="path[4]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190757.jpg"/>
      <property name="path[1]" value="C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python\calibration images\2019-01-18-190557.jpg"/>
    </edu.wpi.grip.core.sources.MultiImageFileSource>
  </sources>
  <steps>
    <edu.wpi.grip.core.Step name="HSV Threshold">
      <edu.wpi.grip.core.sockets.InputSocketImpl step="0" socket="0"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="0" socket="1">
        <value>
          <double>59.89208633093525</double>
          <double>86.06060606060603</double>
        </value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="0" socket="2">
        <value>
          <double>105.48561151079136</double>
          <double>255.0</double>
        </value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="0" socket="3">
        <value>
          <double>68.79496402877697</double>
          <double>255.0</double>
        </value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="0" socket="0" previewed="false"/>
    </edu.wpi.grip.core.Step>
    <edu.wpi.grip.core.Step name="CV dilate">
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="0"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="1"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="2"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="3">
        <value>3.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="4">
        <value>BORDER_CONSTANT</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="5"/>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="1" socket="0" previewed="false"/>
    </edu.wpi.grip.core.Step>
    <edu.wpi.grip.core.Step name="CV erode">
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="0"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="1"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="2"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="3">
        <value>2.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="4">
        <value>BORDER_CONSTANT</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="5"/>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="2" socket="0" previewed="false"/>
    </edu.wpi.grip.core.Step>
    <edu.wpi.grip.core.Step name="Find Contours">
      <edu.wpi.grip.core.sockets.InputSocketImpl step="3" socket="0"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="3" socket="1">
        <value>false</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="3" socket="0" previewed="false"/>
    </edu.wpi.grip.core.Step>
    <edu.wpi.grip.core.Step name="Filter Contours">
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="0"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="1">
        <value>700.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="2">
        <value>0.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="3">
        <value>20.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="4">
        <value>10000.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="5">
        <value>20.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="6">
        <value>10000.0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="7">
        <value>
          <double>74.64028776978418</double>
          <int>100</int>
        </value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="8">
        <value>1000000</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="9">
        <value>0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="10">
        <value>0</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="11">
        <value>1000</value>
      </edu.wpi.grip.core.sockets.InputSocketImpl>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="4" socket="0" previewed="true"/>
    </edu.wpi.grip.core.Step>
  </steps>
  <connections>
    <edu.wpi.grip.core.Connection>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="2" socket="0" previewed="false"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="3" socket="0"/>
    </edu.wpi.grip.core.Connection>
    <edu.wpi.grip.core.Connection>
      <edu.wpi.grip.core.sockets.OutputSocketImpl source="0" socket="0" previewed="true"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="0" socket="0"/>
    </edu.wpi.grip.core.Connection>
    <edu.wpi.grip.core.Connection>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="0" socket="0" previewed="false"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="1" socket="0"/>
    </edu.wpi.grip.core.Connection>
    <edu.wpi.grip.core.Connection>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="3" socket="0" previewed="false"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="4" socket="0"/>
    </edu.wpi.grip.core.Connection>
    <edu.wpi.grip.core.Connection>
      <edu.wpi.grip.core.sockets.OutputSocketImpl step="1" socket="0" previewed="false"/>
      <edu.wpi.grip.core.sockets.InputSocketImpl step="2" socket="0"/>
    </edu.wpi.grip.core.Connection>
  </connections>
  <settings>
    <teamNumber>0</teamNumber>
    <publishAddress>roboRIO-0-FRC.local</publishAddress>
    <deployAddress>roboRIO-0-FRC.local</deployAddress>
    <deployDir>/home/lvuser</deployDir>
    <deployUser>lvuser</deployUser>
    <deployJavaHome>/usr/local/frc/JRE/</deployJavaHome>
    <deployJvmOptions>-Xmx50m -XX:-OmitStackTraceInFastThrow -XX:+HeapDumpOnOutOfMemoryError -XX:MaxNewSize=16m</deployJvmOptions>
  </settings>
  <codeGenerationSettings>
    <language>Python</language>
    <className>GripRetroreflectivePipeline</className>
    <implementWpilibPipeline>false</implementWpilibPipeline>
    <saveDir>C:\Users\Albert Lin\Desktop\FRC 2019 Vision Code Python</saveDir>
    <packageName></packageName>
    <moduleName>grip</moduleName>
  </codeGenerationSettings>
</edu.wpi.grip.core.Pipeline>