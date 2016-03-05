
######################################DataBase Migrtion Script from SQLServer to Postgres###########################################################
########################################Developed By Ayman ELgharabawy 25/2/1016######################################################################
from os import getenv
import pyodbc
import psycopg2
import sqlite3
from sqlite3 import OperationalError

dbname="postgres";

######################################Opn the DB Connctions for source and destination#########################################################
##############################################################################################################
conn1 = pyodbc.connect('DRIVER={SQL Server};SERVER=KOTOBI\KOTOBI;DATABASE=newkotob;UID=sa;PWD=Cairo_123') 
cursor = conn1.cursor();
conn2 = psycopg2.connect("host=127.0.0.1 dbname=kotob user=postgres password=postgres");
cur = conn2.cursor();
msg="";

cur.execute('SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid()');
cur.execute(open("kotob.sql", "r").read());
conn2.commit();
######################################PublicationTypes Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('######################################PublicationTypes Table Migration########################################');
##########################################Transform Data#######################################
cursor.execute('SELECT [id], [Publication_En],[Publication_Ar]  FROM [dbo].[PublicationTypes]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."publicationtypes" (id, publication_en,publication_ar) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();

##############################################################################################################
##############################################################################################################

######################################PublicationStatus Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('######################################PublicationStatus Table Migration########################################');
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [Status_En],[Status_Ar]  FROM [dbo].[PublicationStatus]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."publicationstatus" (id, status_en,status_ar) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();

##############################################################################################################
##############################################################################################################

  

######################################PeriodicalIntervals Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [Interval_En],[Interval_Ar]  FROM [dbo].[periodicalintervals]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."periodicalintervals" (id, interval_en,interval_ar) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();

##############################################################################################################


######################################PeriodicalTypes Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [Type_En],[Type_Ar ] FROM [dbo].[PeriodicalTypes]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."periodicaltypes" (id, Type_En,Type_Ar) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();

##############################################################################################################


######################################SubscriptionType Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [Type_En],[Type_Ar] ,[PeriodicalIntervalId] ,[NumberOfWeeks] FROM [dbo].[SubscriptionTypes]');
for row in cursor:
    print('row[0] = %r' % (row[3],))
    cur.execute('INSERT INTO public."subscriptiontype" (id, type_en,type_ar,id_periodicalintervals,numberofweeks) VALUES (%s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4]));
conn2.commit();

##############################################################################################################


######################################producttag Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [name] FROM [dbo].[producttag]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."producttag" (id, name) VALUES (%s, %s)',(row[0], row[1]));
conn2.commit();

##############################################################################################################

######################################ProductCategory Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [name],[parentcategoryid ],[description] ,[HasDiscountsApplied] ,[published], [deleted],[pictureid],[pagesize],[AllowCustomersToSelectPageSize],[showonhomepage],[displayorder],[createdonutc],[updatedonutc] FROM [dbo].[Category]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
cur.execute('INSERT INTO public."productcategory" (id, name,parentcategoryid ,description ,hasdiscountsapplied ,published, deleted,pictureid,pagesize,allowcustomertoselectpagesize,showonhomepage,displayorder,createdonutc,updatedonutc)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]));
conn2.commit();

##############################################################################################################



######################################Customer Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('###################################### Customer Table Migration########################################');

######################################Clear Destination#######################################################
print('######################################many_CustomerRole_has_many_Customer Table Migration########################################');
######################################CustomerRole Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('######################################CustomerRole Table Migration########################################');
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [name] ,[FreeShipping]  ,[Active] ,[IsSystemRole] ,[SystemName] FROM [dbo].[CustomerRole]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."customerrole" (id, name , freeshipping,active ,isSystemrole ,systemname) VALUES (%s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5]));
conn2.commit();

##############################################################################################################




##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [CustomerGuid], [username] , [email] , [password] , [Deleted] , [IsSystemAccount] ,[Systemname] ,[lastipaddress],[createdonUtc], [lastloginDateUtc],[PublisherId],[pictureid] , [PreferredEmail] , [LinkedCustomerId] , [LinkDateUtc] , [LoginType] ,[IsMobileVerified] , [DefaultPayment] ,[DefaultPaymentMobile] FROM [dbo].[Customer]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."customer" (id, customerguid,  username , email , password , deleted , isSystemAccount ,systemname   ,lastipaddress,createdonutc, lastlogindateutc,publisherid,pictureid , preferredemail , linkedcustomerid , linkdateutc , logintype ,ismobileverified , defaultpayment ,defaultpaymentmobile) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19]));
conn2.commit();

##############################################################################################################




######################################Customer_CustomerRole_Mapping Table Migration#########################################################
##############################################################################################################

##########################################Transform Data#######################################
cursor.execute('SELECT [Customer_Id], [CustomerRole_Id] FROM [dbo].[Customer_CustomerRole_Mapping]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."many_CustomerRole_has_many_Customer" (id_customer,id_customerrole) VALUES (%s, %s)',(row[0], row[1]));
conn2.commit();

##############################################################################################################



######################################Product Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################


######################################Customer_CustomerRole_Mapping Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('######################################orginalfrom Table Migration########################################');
##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [OrginalFrom_En] ,[OrginalFrom_Ar] FROM [dbo].[orginalfrom]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."orginalfrom" (id,orginalfrom_en,orginalfrom_ar) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();

##############################################################################################################



##############################################################################################################
######################################Publisher Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
print('###################################### publisher Table Migration########################################');

##########################################Transform Data#######################################
cursor.execute('SELECT [id] , [Customer_Id] , [publisherName] , [website] , [foundationyear] , [About] , [MainOfficeAddress] , [SPOCEmail] , [SPOCFirstName] , [SPOCLastName] , [SPOCMobileNumber] , [ActivationStartDate] , [ActivationEndDate]  , [PublicationTypeId] , [Deleted] , [Suspended]  FROM [dbo].[publisher]');
for row in cursor:
    print('row[13] = %r' % (row[13],))
    if row[13] == 0:
     row[13] = 1;
    cur.execute('INSERT INTO public."publisher" (id , id_customer , name , website , foundationyear , About , mainofficeaddress , spocemail , spocfirstname , spoclastname , spocmobilenumber , activationstartdate , activationenddate  , id_publicationtypes, deleted , suspended )   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]));
conn2.commit();

##############################################################################################################

print('######################################Product Table Migration########################################');

##########################################Transform Data#######################################
cursor.execute('SELECT [Id], [name], [ShortDescription] ,[fulldescription] ,[ProductTemplateId],[showonhomepage],[AllowCustomerReviews],[ApprovedRatingSum],[NotApprovedRatingSum],[ApprovedTotalReviews],[NotApprovedTotalReviews],[Sku] , [IsGiftCard] ,[IsDownload] ,[UnlimitedDownloads] , [MaxNumberOfDownloads] , [DownloadExpirationDays] , [OrderMinimumQuantity] , [OrderMaximumQuantity] , [AllowedQuantities] , [price] , [Oldprice] , [productcost] , [specialprice] ,[SpecialPriceStartDateTimeUtc] , [SpecialPriceEndDateTimeUtc] ,[HasDiscountsApplied] , [Displayorder],[published] , [deleted] , [createdonutc] , [updatedonutc] , [PublisherId] ,[PublicationTypeId] , [PeriodicalIntervalId] , [OrginalFromId],[IsVersionPublished] , [NumberofTrials] ,[PublishDate] , [AddedToSelectedByKotob] ,[RejectionReason],[IsArabicPublication] ,[PublicationYear] , [FinalPrice] ,[ContentType] ,[IsPublicDomain] ,[IsRePublishRequired] ,[IsBundle]  ,[VersionNumber] ,[IsSellableAbroad] ,[customerid] , [useragreementtext]  FROM [dbo].[product]');
for row in cursor: 
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."product" (id, name,shortdescription ,fulldescription,ProductTemplateId,showonhomepage,allowcustomerreviews,approvedratingsum,notapprovedratingsum   , approvedtotalreviews , notapprovedtotalreviews , sku , isgiftcard , isdownload ,unlimiteddownloads , maxnumberofdownloads , downloadexpirationdays , orderminimumquantity , ordermaximumquantity ,allowedquantities , price, oldprice ,productcost , specialprice , specialpricestartdatetimeutc , specialpriceenddatetimeutc , hasdiscountsapplied ,displayorder, published , deleted,createdonutc,updatedonutc ,id_Publisher,id_Publicationtypes ,id_periodicalintervals ,id_orginalfrom ,isversionpublished ,numberoftrials , publishdate ,addedtoselectedbykotob , rejectionreason , isarabicpublication ,publicationyear  , finalprice , contenttype , ispublicdomain , isrepublishrequired , isbundle ,versionnumber ,issellableabroad ,id_customer , useragreementtext)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26] ,row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50],row[51]));
conn2.commit();

##############################################################################################################Sk





##############################################################################################################
######################################Order Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id] , [orderguid],[customerid] ,[orderstatusid],[paymentstatusid], [paymentmethodsystemname] ,[customercurrencycode],[currencyrate],[CustomerTaxDisplayTypeId],[OrderSubtotalInclTax],[ordersubtotalexcltax] ,[PaymentMethodAdditionalFeeInclTax] , [PaymentMethodAdditionalFeeExclTax] ,[TaxRates] , [OrderTax],[OrderDiscount], [OrderTotal] , [RefundedAmount] , [Customerip], [AllowStoringCreditCardNumber] , [CardType] , [CardName] , [CardNUmber] , [MaskedCreditCardNumber] ,[CardCvv2] , [CardExpirationMonth] ,[CardExpirationYear] , [PaidDateUtc],[Deleted]  ,[createdonUtc] , [IsGiftBook] FROM [dbo].[Order]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."purchaseorder" (id , orderguid,id_customer ,orderstatus,paymentstatus, paymentmethodsystemname ,customercurrencycode,currencyrate,customertaxdisplaytypename,ordersubtotalincltax,ordersubtotalexcltax ,paymentmethodadditionalfeeincltax , paymentmethodadditionalfeeexcltax ,taxrates , ordertax,orderdiscount, ordertotal , refundedamount , customerip, allowStoringcreditcardnumber , cardtype , cardname , cardnumber , maskedcreditcardnumber ,cardcvv2 , cardexpirationmonth , cardexpirationyear , paiddateutc,deleted  ,createdonUtc , isgiftbook) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30]));
conn2.commit();

##############################################################################################################

##############################################################################################################
######################################OrderStatus Status Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id] ,[orderid], [note],[DisplayToCustomer],[createdonUtc] FROM [dbo].[OrderNote]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."ordernote" (id ,id_purchaseorder ,  note,DisplayToCustomer,createdonUtc) VALUES (%s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4]));
conn2.commit();

##############################################################################################################



######################################purchaseorderitem Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT oi.[id] , oi.[OrderItemGuid],oi.[OrderId],oi.[ProductId],oi.[Quantity],oi.[UnitPriceInclTax],oi.[UnitPriceExclTax] ,oi.[PriceInclTax] ,oi.[PriceExclTax] ,oi.[DiscountAmountInclTax] ,oi.[DiscountAmountExclTax] , oi.[OriginalProductCost] , oi.[AttributeDescription] , oi.[IsDownloadActivated] ,oi.[LicenseDownloadId] , oi.[BundleId] ,oi.[IsBundle] , oi.[IsHidden] ,oi.[HideDate] FROM [dbo].[orderitem] oi ,[dbo].[Order] o  , [dbo].[Product] p where oi.orderid=o.id and oi.productid=p.id');
for row in cursor:
    print('row[2] = %r' % (row[2],))
    cur.execute('INSERT INTO public."purchaseorderitem" (id,orderitemguid,id_purchaseorder , id_product , quantity , unitpriceincltax ,unitpriceexcltax ,priceincltax ,priceexcltax ,discountamountincltax ,discountamountexcltax , originalproductcost , attributedescription , isDownloadactivated ,licensedownloadid ,bundleid , isbundle ,ishidden ,hidedate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18]));
conn2.commit();


######################################CustomerPeriodicalSubscriptions Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT per.[id] ,  per.[CustomerId], per.[Subscriptiontypeid ], per.[startdate], per.[enddate], per.[deleted], per.[orderitemid] FROM [dbo].[CustomerPeriodicalSubscriptions]  per , [dbo].[orderitem] poi  where per.orderitemid=poi.id');
for row in cursor:
    print('row[6] = %r' % (row[6],))
    cur.execute('INSERT INTO public."customerperiodicalsubscription" (id,id_customer,subscriptiontypeid , startdate , enddate , deleted , id_purchaseorderitem) VALUES (%s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6]));
conn2.commit();




######################################many_customerperiodicalsubscription_has_many_product Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [productid], [SubscriptionTypeId],[PriceLE],[PriceLoyaltyPoints],[IsDefault] FROM [dbo].[Product_SubscriptionType_Mapping]');
for row in cursor:
    print('row[3] = %r' % (row[3],))
    cur.execute('INSERT INTO public."many_customerperiodicalsubscription_has_many_product" (id_product,id_customerperiodicalsubscription , pricele , priceloyaltypoints , isdefault) VALUES (%s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4]));
conn2.commit();


##############################################################################################################



##############################################################################################################
######################################Author Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id] ,[name] , [name_ar] , [description] , [description_ar] , [born] , [died] , [occupationid] , [CountryOfBirthId] , [active] , [deleted] , [wikilink] , [pictureid] FROM [dbo].[Author]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."author"(id ,name , name_ar , description , description_ar , born , died , id_occupation , countryofbirthid , active , deleted , wikilink , pictureid  )   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]));
conn2.commit();

##############################################################################################################



######################################CustomerPeriodicalSubscriptions Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT cps.[id] , cps.[CustomerId],cps.[Subscriptiontypeid ],cps.[startdate],cps.[enddate],cps.[deleted],cps.[orderitemid] FROM [dbo].[CustomerPeriodicalSubscriptions] cps , [dbo].[orderitem] poi where poi.id = cps.orderitemid');
for row in cursor:
    print('row[6] = %r' % (row[6],))
    cur.execute('INSERT INTO public."customerperiodicalsubscription" (id,id_customer,subscriptiontypeid , startdate , enddate , deleted , id_purchaseorderitem) VALUES (%s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6]));
conn2.commit();




######################################many_customerperiodicalsubscription_has_many_product Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [productid], [SubscriptionTypeId],[PriceLE],[PriceLoyaltyPoints],[IsDefault] FROM [dbo].[Product_SubscriptionType_Mapping]');
for row in cursor:
    print('row[3] = %r' % (row[3],))
    cur.execute('INSERT INTO public."many_customerperiodicalsubscription_has_many_product" (id_product,id_customerperiodicalsubscription , pricele , priceloyaltypoints , isdefault) VALUES (%s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4]));
conn2.commit();


##############################################################################################################
######################################occupation Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id], [occupation_en],[occupation_ar] FROM [dbo].[occupation]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."occupation" (id,occupation_en , occupation_ar ) VALUES (%s, %s, %s)',(row[0], row[1], row[2]));
conn2.commit();



##############################################################################################################
######################################country Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id], [Name],[AllowsBilling] , [AllowsShipping] , [TwoLetterIsoCode] , [ThreeLetterIsoCode] , [NumericIsoCode] ,[SubjectToVat] , [Published] ,[DisplayOrder] ,[GroupId] FROM [dbo].[country]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."country" (id,name , allowbilling , allowshipping , twoletterisocode , threeletterisocode , numberisocode , subjecttovat , published , displayorder , groupid  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]));
conn2.commit();


##############################################################################################################
######################################Author Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id] ,[name] , [name_ar] , [description] , [description_ar] , [born] , [died] , [occupationid] , [CountryOfBirthId] , [active] , [deleted] , [wikilink] , [pictureid] FROM [dbo].[Author]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    if row[7] ==0:
        row[7]=3
    cur.execute('INSERT INTO public."author"(id ,name_en , name_ar , description_en , description_ar , birthdate , deaddate , id_occupation , id_country , active , deleted , wikilink , pictureid  )   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]));
conn2.commit();

##############################################################################################################

##############################################################################################################
######################################content Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id], [Author],[ContentKey] , [EncryptionKey] ,[Title] ,[Type] ,[Issue] ,[ISBN] , [Status] , [NotificationStatus] , [NumberOfTries] , [UCMID] ,[Publisher]  ,[ContentType] FROM [dbo].[Content]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."content" (id,author ,contentkey , encryptionkey , title ,type, issue , isbn , status ,notificationstatus , numberoftries , ucmid , publisher , contenttype  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]));
conn2.commit();

##############################################################################################################
######################################readerchecksum Table Migration#########################################################
##############################################################################################################
######################################Clear Destination#######################################################
##########################################Transform Data#######################################
cursor.execute('SELECT [id], [Platform], [Version],[CheckSum] FROM [dbo].[readerchecksum]');
for row in cursor:
    print('row[0] = %r' % (row[0],))
    cur.execute('INSERT INTO public."readerchecksum" (id,platform ,version , checksum  ) VALUES (%s, %s, %s, %s)',(row[0], row[1], row[2], row[3]));
conn2.commit();

cur.close();
cursor.close();

conn1.close();
conn2.close();
