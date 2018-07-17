#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(id, mainEmail, passw):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Thank You For Visiting The Drexel Smart House!"
	msg['From'] = mainEmail
	msg['To'] = id.lower()+'@drexel.edu'

	html = """\
		<!doctype html>
		<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
			<head>
				<!-- NAME: 1 COLUMN -->
				<!--[if gte mso 15]>
				<xml>
					<o:OfficeDocumentSettings>
					<o:AllowPNG/>
					<o:PixelsPerInch>96</o:PixelsPerInch>
					</o:OfficeDocumentSettings>
				</xml>
				<![endif]-->
				<meta charset="UTF-8">
				<meta http-equiv="X-UA-Compatible" content="IE=edge">
				<meta name="viewport" content="width=device-width, initial-scale=1">
				
			<style type="text/css">
				p{
					margin:10px 0;
					padding:0;
				}
				table{
					border-collapse:collapse;
				}
				h1,h2,h3,h4,h5,h6{
					display:block;
					margin:0;
					padding:0;
				}
				img,a img{
					border:0;
					height:auto;
					outline:none;
					text-decoration:none;
				}
				body,#bodyTable,#bodyCell{
					height:100%;
					margin:0;
					padding:0;
					width:100%;
				}
				.mcnPreviewText{
					display:none !important;
				}
				#outlook a{
					padding:0;
				}
				img{
					-ms-interpolation-mode:bicubic;
				}
				table{
					mso-table-lspace:0pt;
					mso-table-rspace:0pt;
				}
				.ReadMsgBody{
					width:100%;
				}
				.ExternalClass{
					width:100%;
				}
				p,a,li,td,blockquote{
					mso-line-height-rule:exactly;
				}
				a[href^=tel],a[href^=sms]{
					color:inherit;
					cursor:default;
					text-decoration:none;
				}
				p,a,li,td,body,table,blockquote{
					-ms-text-size-adjust:100%;
					-webkit-text-size-adjust:100%;
				}
				.ExternalClass,.ExternalClass p,.ExternalClass td,.ExternalClass div,.ExternalClass span,.ExternalClass font{
					line-height:100%;
				}
				a[x-apple-data-detectors]{
					color:inherit !important;
					text-decoration:none !important;
					font-size:inherit !important;
					font-family:inherit !important;
					font-weight:inherit !important;
					line-height:inherit !important;
				}
				#bodyCell{
					padding:10px;
				}
				.templateContainer{
					max-width:600px !important;
				}
				a.mcnButton{
					display:block;
				}
				.mcnImage,.mcnRetinaImage{
					vertical-align:bottom;
				}
				.mcnTextContent{
					word-break:break-word;
				}
				.mcnTextContent img{
					height:auto !important;
				}
				.mcnDividerBlock{
					table-layout:fixed !important;
				}
				body,#bodyTable{
					background-color:#FAFAFA;
				}
				#bodyCell{
					border-top:0;
				}
				.templateContainer{
					border:0;
				}
				h1{
					color:#202020;
					font-family:Helvetica;
					font-size:26px;
					font-style:normal;
					font-weight:bold;
					line-height:125%;
					letter-spacing:normal;
					text-align:left;
				}
				h2{
					color:#202020;
					font-family:Helvetica;
					font-size:22px;
					font-style:normal;
					font-weight:bold;
					line-height:125%;
					letter-spacing:normal;
					text-align:left;
				}
				h3{
					color:#202020;
					font-family:Helvetica;
					font-size:20px;
					font-style:normal;
					font-weight:bold;
					line-height:125%;
					letter-spacing:normal;
					text-align:left;
				}
				h4{
					color:#202020;
					font-family:Helvetica;
					font-size:18px;
					font-style:normal;
					font-weight:bold;
					line-height:125%;
					letter-spacing:normal;
					text-align:left;
				}
				#templatePreheader{
					background-color:#FAFAFA;
					background-image:none;
					background-repeat:no-repeat;
					background-position:center;
					background-size:cover;
					border-top:0;
					border-bottom:0;
					padding-top:9px;
					padding-bottom:9px;
				}
				#templatePreheader .mcnTextContent,#templatePreheader .mcnTextContent p{
					color:#656565;
					font-family:Helvetica;
					font-size:12px;
					line-height:150%;
					text-align:left;
				}
				#templatePreheader .mcnTextContent a,#templatePreheader .mcnTextContent p a{
					color:#656565;
					font-weight:normal;
					text-decoration:underline;
				}
				#templateHeader{
					background-color:#FFFFFF;
					background-image:none;
					background-repeat:no-repeat;
					background-position:center;
					background-size:cover;
					border-top:0;
					border-bottom:0;
					padding-top:9px;
					padding-bottom:0;
				}
				#templateHeader .mcnTextContent,#templateHeader .mcnTextContent p{
					color:#202020;
					font-family:Helvetica;
					font-size:16px;
					line-height:150%;
					text-align:left;
				}
				#templateHeader .mcnTextContent a,#templateHeader .mcnTextContent p a{
					color:#2BAADF;
					font-weight:normal;
					text-decoration:underline;
				}
				#templateBody{
					background-color:#FFFFFF;
					background-image:none;
					background-repeat:no-repeat;
					background-position:center;
					background-size:cover;
					border-top:0;
					border-bottom:2px solid #EAEAEA;
					padding-top:0;
					padding-bottom:9px;
				}
				#templateBody .mcnTextContent,#templateBody .mcnTextContent p{
					color:#202020;
					font-family:Helvetica;
					font-size:16px;
					line-height:150%;
					text-align:left;
				}
				#templateBody .mcnTextContent a,#templateBody .mcnTextContent p a{
					color:#2BAADF;
					font-weight:normal;
					text-decoration:underline;
				}
				#templateFooter{
					background-color:#FAFAFA;
					background-image:none;
					background-repeat:no-repeat;
					background-position:center;
					background-size:cover;
					border-top:0;
					border-bottom:0;
					padding-top:9px;
					padding-bottom:9px;
				}
				#templateFooter .mcnTextContent,#templateFooter .mcnTextContent p{
					color:#656565;
					font-family:Helvetica;
					font-size:12px;
					line-height:150%;
					text-align:center;
				}
				#templateFooter .mcnTextContent a,#templateFooter .mcnTextContent p a{
					color:#656565;
					font-weight:normal;
					text-decoration:underline;
				}
			@media only screen and (min-width:768px){
				.templateContainer{
					width:600px !important;
				}

		}	@media only screen and (max-width: 480px){
				body,table,td,p,a,li,blockquote{
					-webkit-text-size-adjust:none !important;
				}

		}	@media only screen and (max-width: 480px){
				body{
					width:100% !important;
					min-width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				#bodyCell{
					padding-top:10px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnRetinaImage{
					max-width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImage{
					width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnCartContainer,.mcnCaptionTopContent,.mcnRecContentContainer,.mcnCaptionBottomContent,.mcnTextContentContainer,.mcnBoxedTextContentContainer,.mcnImageGroupContentContainer,.mcnCaptionLeftTextContentContainer,.mcnCaptionRightTextContentContainer,.mcnCaptionLeftImageContentContainer,.mcnCaptionRightImageContentContainer,.mcnImageCardLeftTextContentContainer,.mcnImageCardRightTextContentContainer,.mcnImageCardLeftImageContentContainer,.mcnImageCardRightImageContentContainer{
					max-width:100% !important;
					width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnBoxedTextContentContainer{
					min-width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageGroupContent{
					padding:9px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnCaptionLeftContentOuter .mcnTextContent,.mcnCaptionRightContentOuter .mcnTextContent{
					padding-top:9px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageCardTopImageContent,.mcnCaptionBottomContent:last-child .mcnCaptionBottomImageContent,.mcnCaptionBlockInner .mcnCaptionTopContent:last-child .mcnTextContent{
					padding-top:18px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageCardBottomImageContent{
					padding-bottom:9px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageGroupBlockInner{
					padding-top:0 !important;
					padding-bottom:0 !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageGroupBlockOuter{
					padding-top:9px !important;
					padding-bottom:9px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnTextContent,.mcnBoxedTextContentColumn{
					padding-right:18px !important;
					padding-left:18px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnImageCardLeftImageContent,.mcnImageCardRightImageContent{
					padding-right:18px !important;
					padding-bottom:0 !important;
					padding-left:18px !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcpreview-image-uploader{
					display:none !important;
					width:100% !important;
				}

		}	@media only screen and (max-width: 480px){
				h1{
					font-size:22px !important;
					line-height:125% !important;
				}

		}	@media only screen and (max-width: 480px){
				h2{
					font-size:20px !important;
					line-height:125% !important;
				}

		}	@media only screen and (max-width: 480px){
				h3{
					font-size:18px !important;
					line-height:125% !important;
				}

		}	@media only screen and (max-width: 480px){
				h4{
					font-size:16px !important;
					line-height:150% !important;
				}

		}	@media only screen and (max-width: 480px){
				.mcnBoxedTextContentContainer .mcnTextContent,.mcnBoxedTextContentContainer .mcnTextContent p{
					font-size:14px !important;
					line-height:150% !important;
				}

		}	@media only screen and (max-width: 480px){
				#templatePreheader{
					display:block !important;
				}

		}	@media only screen and (max-width: 480px){
				#templatePreheader .mcnTextContent,#templatePreheader .mcnTextContent p{
					font-size:14px !important;
					line-height:150% !important;
				}

		}	@media only screen and (max-width: 480px){
				#templateHeader .mcnTextContent,#templateHeader .mcnTextContent p{
					font-size:16px !important;
					line-height:150% !important;
				}

		}	@media only screen and (max-width: 480px){
				#templateBody .mcnTextContent,#templateBody .mcnTextContent p{
					font-size:16px !important;
					line-height:150% !important;
				}

		}	@media only screen and (max-width: 480px){
				#templateFooter .mcnTextContent,#templateFooter .mcnTextContent p{
					font-size:14px !important;
					line-height:150% !important;
				}

		}</style></head>
			<body>
				<center>
					<table align="center" border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable">
						<tr>
							<td align="center" valign="top" id="bodyCell">
								<!-- BEGIN TEMPLATE // -->
								<!--[if (gte mso 9)|(IE)]>
								<table align="center" border="0" cellspacing="0" cellpadding="0" width="600" style="width:600px;">
								<tr>
								<td align="center" valign="top" width="600" style="width:600px;">
								<![endif]-->
								<table border="0" cellpadding="0" cellspacing="0" width="100%" class="templateContainer">
									<tr>
										<td valign="top" id="templatePreheader"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnImageBlock" style="min-width:100%;">
			<tbody class="mcnImageBlockOuter">
					<tr>
						<td valign="top" style="padding:9px" class="mcnImageBlockInner">
							<table align="left" width="100%" border="0" cellpadding="0" cellspacing="0" class="mcnImageContentContainer" style="min-width:100%;">
								<tbody><tr>
									<td class="mcnImageContent" valign="top" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0; text-align:center;">
										
											
												<img align="center" alt="" src="https://gallery.mailchimp.com/479ca464415af2c74a0c98259/images/79066081-71ff-4f2f-bef2-649c1192c53f.png" width="564" style="max-width:785px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" class="mcnImage">
											
										
									</td>
								</tr>
							</tbody></table>
						</td>
					</tr>
			</tbody>
		</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
			<tbody class="mcnDividerBlockOuter">
				<tr>
					<td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
						<table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EAEAEA;">
							<tbody><tr>
								<td>
									<span></span>
								</td>
							</tr>
						</tbody></table>
		<!--            
						<td class="mcnDividerBlockInner" style="padding: 18px;">
						<hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
		-->
					</td>
				</tr>
			</tbody>
		</table></td>
									</tr>
									<tr>
										<td valign="top" id="templateHeader"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnTextBlock" style="min-width:100%;">
			<tbody class="mcnTextBlockOuter">
				<tr>
					<td valign="top" class="mcnTextBlockInner" style="padding-top:9px;">
						<!--[if mso]>
						<table align="left" border="0" cellspacing="0" cellpadding="0" width="100%" style="width:100%;">
						<tr>
						<![endif]-->
						
						<!--[if mso]>
						<td valign="top" width="600" style="width:600px;">
						<![endif]-->
						<table align="left" border="0" cellpadding="0" cellspacing="0" style="max-width:100%; min-width:100%;" width="100%" class="mcnTextContentContainer">
							<tbody><tr>
								
								<td valign="top" class="mcnTextContent" style="padding-top:0; padding-right:18px; padding-bottom:9px; padding-left:18px;">
								
									<h1 style="text-align: center;"><strong><span style="font-family:helvetica neue,helvetica,arial,verdana,sans-serif">Welcome to Drexel Smart House!&nbsp;</span></strong></h1>

		<div style="text-align: center;"><br>
		<span style="font-family:helvetica neue,helvetica,arial,verdana,sans-serif"><span style="font-size:14px">We would like to thank you for your interest in Drexel Smart House! You have received this message because you have signed into the Smart House for the first time, and as a new member we would like to welcome you officially.&nbsp;As a new member, be sure to find us on Slack and Facebook to stay updated with any events we are having, and stay tuned for future newsletters.&nbsp;<br>
		<br>
		If you have not already done so,&nbsp;also be sure to join us on <a href="https://dragonlink.drexel.edu/organization/drexel-smart-house" target="_blank">DragonLink</a><br>
		<br>
		Sincerely,&nbsp;<br>
		Drexel Smart House Executive Team</span></span></div>

								</td>
							</tr>
						</tbody></table>
						<!--[if mso]>
						</td>
						<![endif]-->
						
						<!--[if mso]>
						</tr>
						</table>
						<![endif]-->
					</td>
				</tr>
			</tbody>
		</table></td>
									</tr>
									<tr>
										<td valign="top" id="templateBody"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
			<tbody class="mcnDividerBlockOuter">
				<tr>
					<td class="mcnDividerBlockInner" style="min-width:100%; padding:18px;">
						<table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EAEAEA;">
							<tbody><tr>
								<td>
									<span></span>
								</td>
							</tr>
						</tbody></table>
		<!--            
						<td class="mcnDividerBlockInner" style="padding: 18px;">
						<hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
		-->
					</td>
				</tr>
			</tbody>
		</table></td>
									</tr>
									<tr>
										<td valign="top" id="templateFooter"><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnCaptionBlock">
			<tbody class="mcnCaptionBlockOuter">
				<tr>
					<td class="mcnCaptionBlockInner" valign="top" style="padding:9px;">
						

		<table align="left" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="282">
			<tbody><tr>
				<td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
				
					
					<a href="https://www.facebook.com/DrexelSmartHouse/notifications/" title="" class="" target="_blank">
					

					<img alt="" src="https://gallery.mailchimp.com/479ca464415af2c74a0c98259/images/d15daed5-0f78-4dab-b76f-4f0263b04d44.png" width="264" style="max-width:1000px;" class="mcnImage">
					</a>
				
				</td>
			</tr>
			<tr>
				<td class="mcnTextContent" valign="top" style="padding:0 9px 0 9px;" width="282">
					Want to get involved? Have questions? Message us on our Facebook page!
				</td>
			</tr>
		</tbody></table>

		<table align="right" border="0" cellpadding="0" cellspacing="0" class="mcnCaptionBottomContent" width="282">
			<tbody><tr>
				<td class="mcnCaptionBottomImageContent" align="center" valign="top" style="padding:0 9px 9px 9px;">
				
					
					<a href="https://join.slack.com/t/drexelsmarthouse/shared_invite/enQtMzE1MzI3NzY4NDAzLTc1NmQxNjFhODI4ODJhMjlhNWIzODdmZDg0MTgwZjI3OGQ2Yjc1NDIxODY4NDJlNmE4MjIyMGZlNGI0ZWQ4YWQ" title="" class="" target="_blank">
					

					<img alt="" src="https://gallery.mailchimp.com/479ca464415af2c74a0c98259/images/2903a70f-a8f8-4e89-9042-dfc77ae003f9.png" width="200" style="max-width:200px;" class="mcnImage">
					</a>
				
				</td>
			</tr>
			<tr>
				<td class="mcnTextContent" valign="top" style="padding:0 9px 0 9px;" width="282">
					Communicate with your team members by joining our Slack channel!
				</td>
			</tr>
		</tbody></table>





					</td>
				</tr>
			</tbody>
		</table><table border="0" cellpadding="0" cellspacing="0" width="100%" class="mcnDividerBlock" style="min-width:100%;">
			<tbody class="mcnDividerBlockOuter">
				<tr>
					<td class="mcnDividerBlockInner" style="min-width: 100%; padding: 10px 18px 25px;">
						<table class="mcnDividerContent" border="0" cellpadding="0" cellspacing="0" width="100%" style="min-width: 100%;border-top: 2px solid #EEEEEE;">
							<tbody><tr>
								<td>
									<span></span>
								</td>
							</tr>
						</tbody></table>
		<!--            
						<td class="mcnDividerBlockInner" style="padding: 18px;">
						<hr class="mcnDividerContent" style="border-bottom-color:none; border-left-color:none; border-right-color:none; border-bottom-width:0; border-left-width:0; border-right-width:0; margin-top:0; margin-right:0; margin-bottom:0; margin-left:0;" />
		-->
					</td>
				</tr>
			</tbody>
		</table></td>
									</tr>
								</table>
								<!--[if (gte mso 9)|(IE)]>
								</td>
								</tr>
								</table>
								<![endif]-->
								<!-- // END TEMPLATE -->
							</td>
						</tr>
					</table>
				</center>
			</body>
		</html>
	"""

	htmlSection = MIMEText(html, 'html')
	msg.attach(htmlSection)
	
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login(mainEmail,passw)
	s.sendmail(mainEmail, id.lower()+'@drexel.edu', msg.as_string())
	s.quit()