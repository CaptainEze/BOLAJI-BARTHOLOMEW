# **Work Flow Implementaions**

# **Phase 1**: Data Collection and Organization
The questionnaire was studied and was divided into 7 segments
    1. Demographics / Background Info (Prefix: D_)
        **Count**: 7 columns

        - D_Gender (1,2)
        - D_Age (Linkert)
        - D_Education (Linkert)
        - D_Position (1,2)
        - ...
    
    2. Technology Usage (Prefix: U_)
        **Count**: 10 columns

        - U_BIM (Linkert)
        - U_IoT (Linkert)
        - ...
    
    
    3. Digital Technology Adoption (Prefix: A_)
        **Count**: 16 columns

        *Application-focused*
        - A_StreamlineData (Linkert)
        - A_BIMPlanning (Linkert)
        - ...
        *Infrastructure*
        - A_HardwareSoftware (Linkert)
        - A_RemoteAccess (Linkert)
        - ...
        *Policy*
        - A_PolicyExistence (Linkert)
        - A_TroubleshootGuidelines (Linkert)
        - ...
    
    
    4. Determinants of Digital Technology Adoption (Prefix: F_)
        **Count**: 31 columns

        *Technological Factors*
        - F_ProjectEfficiency (Linkert)
        - F_ComplexityHindrance (Linkert)
        - ...
        *Organizational Factors*
        - F_FirmSizeInfluence (Linkert)
        - F_AcquisitionEase (Linkert)
        - ...
        *Environmental Factors*
        - F_CompetitorPressure (Linkert)
        - F_RegulatorySupport (Linkert)
        - ...
    
    
    5. Project Delivery Outcomes (Prefix: P_)
        **Count**: 20 columns

        *Time*
        - P_Time_Completion (Linkert)
        - P_Time_RealisticSchedule (Linkert)
        - ...
        *Cost*
        - P_Cost_Completion (Linkert)
        - P_Cost_OverrunManagement (Linkert)
        - ...
        *Quality*
        - P_Quality_Deliverables (Linkert)
        - P_Quality_MinimalDefects (Linkert)
        - ...
        *Safety*
        - P_Safety_Protocols (Linkert)
        - P_Safety_Response (Linkert)
        - ...
    
    
    6. Sustainability (Prefix: S_)
        **Count**: 31 columns

        *Environmental*
        - S_Env_WasteReduction (Linkert)
        - S_Env_MinimalImpact (Linkert)
        - ...
        *Social*
        - S_Social_CommunityEngagement (Linkert)
        - S_Social_SocialEquity (Linkert)
        - ...
        *Governance*
            - Accountability
                - S_Gov_Accountability1 (Linkert)
                - S_Gov_Accountability4 (Linkert)
                - ...
            - Transparency
                - S_Gov_Transparency1 (Linkert)
                - S_Gov_Transparency6 (Linkert)
                - ...
            - Participation
                - S_Gov_Participation1 (Linkert)
                - S_Gov_Participation4 (Linkert)
                - ...
            - Effectiveness
                - S_Gov_Effectiveness1 (Linkert)
                - S_Gov_Effectiveness5 (Linkert)
                - ...
            - Equality
                - S_Gov_Equality1 (Linkert)
                - S_Gov_Equality4 (Linkert)
                - ...


    7. Barriers to Digital Technology Adoption (Prefix: B_)
        **Count**: 23 columns

        - B_LackAwareness (Linkert)
        - B_SatisfactionWithOldMethods (Linkert)
        - B_ClientUnawareness (Linkert)
        - ...


The data values were entered manually using MS Excel. Each questionnaire response to each data rows
Total of `129` data rows were obtained





#  **Phase 2**: Data Cleaning and Preparation

```vba
Sub FillBlanksAndZerosWithColumnMode()
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets(1)

    Dim colRange As Range
    Dim colIndex As Long
    Dim rowIndex As Long
    Dim dict As Object
    Dim cellValue As Variant
    Dim modeValue As Variant
    Dim maxCount As Long

    Application.ScreenUpdating = False
    Application.Calculation = xlCalculationManual

    ' Loop through columns A to EH (1 to 138)
    For colIndex = 1 To 138
        Set dict = CreateObject("Scripting.Dictionary")

        ' Step 1: Build frequency dictionary for the column (excluding row 1 and 0/blank values)
        For rowIndex = 2 To 60
            cellValue = ws.Cells(rowIndex, colIndex).Value
            If Trim(cellValue) <> "" And cellValue <> 0 Then
                If dict.exists(cellValue) Then
                    dict(cellValue) = dict(cellValue) + 1
                Else
                    dict.Add cellValue, 1
                End If
            End If
        Next rowIndex

        ' Step 2: Determine the mode of the column
        maxCount = 0
        modeValue = ""
        For Each Key In dict.Keys
            If dict(Key) > maxCount Then
                maxCount = dict(Key)
                modeValue = Key
            End If
        Next Key

        ' Step 3: Fill blanks or 0s with the mode
        If Not IsEmpty(modeValue) Then
            For rowIndex = 2 To 60
                cellValue = ws.Cells(rowIndex, colIndex).Value
                If Trim(cellValue) = "" Or cellValue = 0 Then
                    ws.Cells(rowIndex, colIndex).Value = modeValue
                End If
            Next rowIndex
        End If
    Next colIndex

    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic

    MsgBox "Completed! All blank and zero cells filled with mode of their columns.", vbInformation
End Sub

