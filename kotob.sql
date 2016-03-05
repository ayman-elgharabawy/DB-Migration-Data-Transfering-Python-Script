--Script Developed By Ayman Elgharabawy for DB Creation
SET check_function_bodies = false;
drop schema public cascade;
create schema public;

-- object: public.product | type: TABLE --
CREATE TABLE public.product(
	id numeric,
	name text,
	format text,
	file_length integer,
	printed_length integer,
	publication_date date,
	thumbnailurl text,
	thump_image_id text,
	collection_id integer,
	notapprovedratingsum integer,
	allowcustomerreviews boolean,
	id_author integer,
	approvedtotalreviews integer,
	createdonutc date,
	notapprovedtotalreviews integer,
	isbundle boolean,
	contenttype text,
	published boolean,
	showonhomepage boolean,
	unlimiteddownloads boolean,
	fulldescription text,
	specialpricestartdatetimeutc date,
	numberoftrials integer,
	rejectionreason text,
	isversionpublished boolean,
	hasdiscountsapplied boolean,
	recurringtotalcycles integer,
	isarabicpublication boolean,
	giftcardtypeid integer,
	specialprice integer,
	deleted boolean,
	specialpriceenddatetimeutc date,
	price integer,
	visibleindividually boolean,
	hassampledownload boolean,
	addedtoselectedbykotob boolean,
	isdownload boolean,
	automaticallyaddrequiredproducts boolean,
	publicationyear integer,
	publishdate date,
	"updatedonUtc" date,
	useragreementtext text,
	approvedratingsum integer,
	requireotherproducts boolean,
	producttemplateid integer,
	downloadexpirationdays integer,
	recurringcyclelength integer,
	admincomment text,
	ordermaximumquantity integer,
	productcost integer,
	noofpages integer,
	isrecurring boolean,
	isgiftcard boolean,
	allowedquantities integer,
	orderminimumquantity smallint,
	version integer,
	displayorder integer,
	ispublicdomain boolean,
	isrepublishrequired boolean,
	issellableabroad boolean,
	callforprice boolean,
	hasuseragreement boolean,
	sku text,
	updatedonutc date,
	shortdescription text,
	hastierprices boolean,
	oldprice integer,
	downloadid integer,
	finalprice integer,
	id_publisher integer,
	maxnumberofdownloads integer,
	versionnumber integer,
	id_customer integer,
	id_publicationtypes integer,
	id_orginalfrom integer,
	id_periodicalintervals integer,
	id_publicationstatus integer,
	id_periodicaltypes integer,
	CONSTRAINT product_prim PRIMARY KEY (id)

);
-- ddl-end --
COMMENT ON COLUMN public.product.name IS 'name of the book/magazine';
-- ddl-end --
-- ddl-end --

-- object: public.publisher | type: TABLE --
CREATE TABLE public.publisher(
	id integer,
	name text,
	description text,
	website text,
	foundationyear varchar,
	about text,
	mainofficeaddress text,
	spocemail varchar,
	spocfirstname text,
	spoclastname text,
	spocmobilenumber text,
	activationstartdate date,
	activationenddate date,
	numberofissueprintperday smallint,
	deleted boolean,
	suspended boolean,
	followersno smallint,
	id_customer integer,
	id_publicationtypes integer,
	CONSTRAINT "Pubprimkey" PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.author | type: TABLE --
CREATE TABLE public.author(
	id integer,
	name_en varchar,
	name_ar varchar,
	description_en text,
	description_ar text,
	birthdate date,
	deaddate date,
	occupation text,
	active boolean,
	deleted boolean,
	wikilink text,
	pictureid varchar,
	id_country integer,
	id_occupation integer,
	CONSTRAINT "AuthPrimKey" PRIMARY KEY (id)

);
-- ddl-end --
-- object: public."many_Author_has_many_Publisher" | type: TABLE --
CREATE TABLE public."many_Author_has_many_Publisher"(
	id_author integer,
	id_publisher integer,
	CONSTRAINT "many_Author_has_many_Publisher_pk" PRIMARY KEY (id_author,id_publisher)

);
-- ddl-end --
-- object: author_fk | type: CONSTRAINT --
ALTER TABLE public."many_Author_has_many_Publisher" ADD CONSTRAINT author_fk FOREIGN KEY (id_author)
REFERENCES public.author (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publisher_fk | type: CONSTRAINT --
ALTER TABLE public."many_Author_has_many_Publisher" ADD CONSTRAINT publisher_fk FOREIGN KEY (id_publisher)
REFERENCES public.publisher (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.customer | type: TABLE --
CREATE TABLE public.customer(
	id integer,
	customerguid text,
	username varchar,
	password text,
	admincomment varchar,
	active boolean,
	deleted boolean,
	issystemaccount boolean,
	systemname varchar,
	ismobileverified boolean,
	preferredemail text,
	createdonutc date,
	"lastactivitydateUtc" date,
	publisherid integer,
	pictureid integer,
	linkedcustomerid integer,
	linkdateutc date,
	logintype integer,
	defaultpayment integer,
	defaultpaymentmobile varchar,
	email text,
	lastlogindateutc date,
	lastipaddress varchar,
	CONSTRAINT custprimkey PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.customerperiodicalsubscription | type: TABLE --
CREATE TABLE public.customerperiodicalsubscription(
	id integer,
	id_customer integer,
	enddate date,
	deleted boolean,
	startdate date,
	subscriptiontypeid integer,
	id_purchaseorderitem integer,
	CONSTRAINT csprimaryk PRIMARY KEY (id)

);
-- ddl-end --
-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.customerperiodicalsubscription ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.purchaseorder | type: TABLE --
CREATE TABLE public.purchaseorder(
	id integer,
	id_customer integer,
	id_product numeric,
	isgiftbook boolean,
	customerip text,
	customercurrencycode text,
	currencyrate integer,
	ordersubtotalincltax integer,
	orderstatusid integer,
	ordersubtotalexcltax integer,
	ordersubtotaldiscountincltax integer,
	paymentmethodsystemname text,
	customertaxdisplaytypename text,
	cardexpirationmonth text,
	cardexpirationyear text,
	ordersubtotaldiscountexcltax integer,
	paymentmethodadditionalfeeincltax smallint,
	paymentmethodadditionalfeeexcltax integer,
	taxrates text,
	ordertax integer,
	orderdiscount integer,
	ordertotal integer,
	refundedamount integer,
	customerlanguageid integer,
	allowstoringcreditcardnumber boolean,
	cardtype text,
	cardname text,
	cardnumber text,
	maskedcreditcardnumber text,
	cardcvv2 text,
	orderguid text,
	orderstatus integer,
	createdonutc date,
	isgiftproduct boolean,
	paymentstatus smallint,
	paiddateutc date,
	deleted boolean,
	CONSTRAINT primidpurchase PRIMARY KEY (id)

);
-- ddl-end --
-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.purchaseorder ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: product_fk | type: CONSTRAINT --
ALTER TABLE public.purchaseorder ADD CONSTRAINT product_fk FOREIGN KEY (id_product)
REFERENCES public.product (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: author_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT author_fk FOREIGN KEY (id_author)
REFERENCES public.author (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.billingprofile | type: TABLE --
CREATE TABLE public.billingprofile(
	id integer,
	creditcard_type varchar,
	creditcard_number text,
	creditcard_issuedate date,
	creditcard_expdate date,
	id_customer integer,
	CONSTRAINT bpprim PRIMARY KEY (id)

);
-- ddl-end --
-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.billingprofile ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.customerrole | type: TABLE --
CREATE TABLE public.customerrole(
	id integer,
	name text,
	systemname text,
	active boolean,
	issystemrole boolean,
	freeshipping boolean,
	CONSTRAINT idprimek PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.customerdevice | type: TABLE --
CREATE TABLE public.customerdevice(
	id integer,
	deviceid text,
	devicename text,
	deleted boolean,
	createdonutc date,
	id_customer integer NOT NULL,
	CONSTRAINT priiddev PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.subscriptiontype | type: TABLE --
CREATE TABLE public.subscriptiontype(
	id integer,
	type_en varchar,
	type_ar varchar,
	numberofweeks smallint,
	id_periodicalintervals integer,
	CONSTRAINT prik PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.productcategory | type: TABLE --
CREATE TABLE public.productcategory(
	id integer,
	name text,
	parentcategoryid integer,
	description text,
	hasdiscountsapplied boolean,
	published boolean,
	deleted boolean,
	pictureid integer,
	pagesize integer,
	allowcustomertoselectpagesize boolean,
	showonhomepage boolean,
	displayorder integer,
	createdonutc date,
	updatedonutc date,
	CONSTRAINT pri PRIMARY KEY (id)

);
-- ddl-end --
-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.customerdevice ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.publicationtypes | type: TABLE --
CREATE TABLE public.publicationtypes(
	id integer,
	publication_en varchar,
	publication_ar varchar,
	CONSTRAINT pprik PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.publicationstatus | type: TABLE --
CREATE TABLE public.publicationstatus(
	id integer,
	status_en text,
	status_ar text,
	CONSTRAINT pubstprimkey PRIMARY KEY (id)

);
-- ddl-end --
-- object: public."many_Product_has_many_ProductCategory" | type: TABLE --
CREATE TABLE public."many_Product_has_many_ProductCategory"(
	id_product numeric,
	id_productcategory integer,
	"IsFeaturedProduct" bit,
	"DisplayOrder" integer,
	CONSTRAINT "many_Product_has_many_ProductCategory_pk" PRIMARY KEY (id_product,id_productcategory)

);
-- ddl-end --
-- object: product_fk | type: CONSTRAINT --
ALTER TABLE public."many_Product_has_many_ProductCategory" ADD CONSTRAINT product_fk FOREIGN KEY (id_product)
REFERENCES public.product (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: productcategory_fk | type: CONSTRAINT --
ALTER TABLE public."many_Product_has_many_ProductCategory" ADD CONSTRAINT productcategory_fk FOREIGN KEY (id_productcategory)
REFERENCES public.productcategory (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.bundle | type: TABLE --
CREATE TABLE public.bundle(
	id integer,
	startdatetime date,
	enddatetime date,
	"Price" integer,
	deleted boolean,
	active boolean,
	published boolean,
	pictureid integer,
	customerid integer,
	name text,
	shortdescription text,
	longdescription text,
	priceperbundle integer,
	CONSTRAINT bundleprimkey PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.purchaseorderitem | type: TABLE --
CREATE TABLE public.purchaseorderitem(
	id integer,
	orderitemguid text,
	quantity integer,
	unitpriceincltax smallint,
	unitpriceexcltax integer,
	priceincltax integer,
	priceexcltax integer,
	id_purchaseorder integer,
	bundleid integer,
	attributedescription text,
	licensedownloadid text,
	ishidden boolean,
	discountamountincltax integer,
	id_product numeric,
	discountamountexcltax integer,
	isdownloadactivated boolean,
	hidedate date,
	originalproductcost integer,
	isbundle boolean,
	CONSTRAINT primkeypoitem PRIMARY KEY (id)

);
-- ddl-end --
-- object: purchaseorder_fk | type: CONSTRAINT --
ALTER TABLE public.purchaseorderitem ADD CONSTRAINT purchaseorder_fk FOREIGN KEY (id_purchaseorder)
REFERENCES public.purchaseorder (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.periodicaltypes | type: TABLE --
CREATE TABLE public.periodicaltypes(
	id integer,
	type_en text,
	type_ar text,
	CONSTRAINT primekey PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.periodicalissues | type: TABLE --
CREATE TABLE public.periodicalissues(
	id integer,
	issuenumber integer,
	issuedate date,
	length integer,
	createdonutc date,
	active boolean,
	deleted boolean,
	isversionpublished boolean,
	numberoftrials integer,
	contenttype text,
	versionnumber integer,
	isrepublishrequired boolean,
	CONSTRAINT periodissprimkey PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.periodicalregionprice | type: TABLE --
CREATE TABLE public.periodicalregionprice(
	id integer,
	"productSubscriptionTypeId" integer,
	"groupId" integer,
	pricele integer,
	finalprice integer,
	priceloyaltypoints integer,
	CONSTRAINT periodicalregionpricepk PRIMARY KEY (id)

);
-- ddl-end --
-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.publisher ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publisher_uq | type: CONSTRAINT --
ALTER TABLE public.publisher ADD CONSTRAINT publisher_uq UNIQUE (id_customer);
-- ddl-end --


-- object: public.discount | type: TABLE --
CREATE TABLE public.discount(
	id integer,
	"discountPercentage" integer,
	"usePercentage" boolean,
	startdateutc date,
	enddateutc date,
	couponcode text,
	requirescouponcode boolean
);
-- ddl-end --
-- object: public.discountappliedtocategories | type: TABLE --
CREATE TABLE public.discountappliedtocategories(
	id integer,
	discount_id integer,
	"category_Id" integer
);
-- ddl-end --
-- object: public."DiscountAppliedToProducts" | type: TABLE --
CREATE TABLE public."DiscountAppliedToProducts"(
	id integer,
	discount_id integer,
	product_id integer
);
-- ddl-end --
-- object: public.occupation | type: TABLE --
CREATE TABLE public.occupation(
	id integer,
	occupation_en text,
	occupation_ar text,
	CONSTRAINT occid PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.orginalfrom | type: TABLE --
CREATE TABLE public.orginalfrom(
	id integer,
	orginalfrom_ar text,
	orginalfrom_en text,
	CONSTRAINT primid PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.productregionprice | type: TABLE --
CREATE TABLE public.productregionprice(
	id integer,
	"productId" integer,
	price integer,
	finalprice integer,
	bundleid integer,
	priceloyaltypoints integer,
	isbundle boolean
);
-- ddl-end --
-- object: public.producttag | type: TABLE --
CREATE TABLE public.producttag(
	id integer,
	name text,
	CONSTRAINT tagpk PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.regiongroup | type: TABLE --
CREATE TABLE public.regiongroup(
	id integer,
	groupname integer,
	pricingfactor integer,
	currencyid integer,
	iddefault boolean,
	groupname_ar text,
	CONSTRAINT prkreg PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.taxcategory | type: TABLE --
CREATE TABLE public.taxcategory(
	id integer,
	name text,
	displayorder text
);
-- ddl-end --
-- object: public.topic | type: TABLE --
CREATE TABLE public.topic(
	id text,
	systemname text,
	includeinsitemap boolean,
	ispasswordprotected integer,
	password text,
	title text,
	body text,
	metakeywords text,
	metadescription text,
	"MetaTitle" text,
	"LimitedToStore" bit,
	CONSTRAINT topicpk PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.periodicalintervals | type: TABLE --
CREATE TABLE public.periodicalintervals(
	id integer,
	interval_ar text,
	interval_en text,
	CONSTRAINT primkeyinterval PRIMARY KEY (id)

);
-- ddl-end --
-- object: public."many_CustomerRole_has_many_Customer" | type: TABLE --
CREATE TABLE public."many_CustomerRole_has_many_Customer"(
	id_customerrole integer,
	id_customer integer,
	CONSTRAINT "many_CustomerRole_has_many_Customer_pk" PRIMARY KEY (id_customerrole,id_customer)

);
-- ddl-end --
-- object: customerrole_fk | type: CONSTRAINT --
ALTER TABLE public."many_CustomerRole_has_many_Customer" ADD CONSTRAINT customerrole_fk FOREIGN KEY (id_customerrole)
REFERENCES public.customerrole (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public."many_CustomerRole_has_many_Customer" ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.ordernote | type: TABLE --
CREATE TABLE public.ordernote(
	id integer,
	note text,
	displaytocustomer boolean,
	createdonutc date,
	id_purchaseorder integer,
	CONSTRAINT orderstpk PRIMARY KEY (id)

);
-- ddl-end --
-- object: purchaseorder_fk | type: CONSTRAINT --
ALTER TABLE public.ordernote ADD CONSTRAINT purchaseorder_fk FOREIGN KEY (id_purchaseorder)
REFERENCES public.purchaseorder (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: periodicalintervals_fk | type: CONSTRAINT --
ALTER TABLE public.subscriptiontype ADD CONSTRAINT periodicalintervals_fk FOREIGN KEY (id_periodicalintervals)
REFERENCES public.periodicalintervals (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publisher_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT publisher_fk FOREIGN KEY (id_publisher)
REFERENCES public.publisher (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: customer_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT customer_fk FOREIGN KEY (id_customer)
REFERENCES public.customer (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publicationtypes_fk | type: CONSTRAINT --
ALTER TABLE public.publisher ADD CONSTRAINT publicationtypes_fk FOREIGN KEY (id_publicationtypes)
REFERENCES public.publicationtypes (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publicationtypes_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT publicationtypes_fk FOREIGN KEY (id_publicationtypes)
REFERENCES public.publicationtypes (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: orginalfrom_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT orginalfrom_fk FOREIGN KEY (id_orginalfrom)
REFERENCES public.orginalfrom (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: periodicalintervals_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT periodicalintervals_fk FOREIGN KEY (id_periodicalintervals)
REFERENCES public.periodicalintervals (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: publicationstatus_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT publicationstatus_fk FOREIGN KEY (id_publicationstatus)
REFERENCES public.publicationstatus (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: periodicaltypes_fk | type: CONSTRAINT --
ALTER TABLE public.product ADD CONSTRAINT periodicaltypes_fk FOREIGN KEY (id_periodicaltypes)
REFERENCES public.periodicaltypes (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: purchaseorderitem_fk | type: CONSTRAINT --
ALTER TABLE public.customerperiodicalsubscription ADD CONSTRAINT purchaseorderitem_fk FOREIGN KEY (id_purchaseorderitem)
REFERENCES public.purchaseorderitem (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: product_fk | type: CONSTRAINT --
ALTER TABLE public.purchaseorderitem ADD CONSTRAINT product_fk FOREIGN KEY (id_product)
REFERENCES public.product (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: public.readerchecksum | type: TABLE --
CREATE TABLE public.readerchecksum(
	id integer,
	platform text,
	version text,
	checksum text,
	CONSTRAINT chpksum PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.content | type: TABLE --
CREATE TABLE public.content(
	id integer,
	author text,
	contentkey text,
	encryptionkey text,
	title text,
	type integer,
	issue text,
	isbn text,
	status text,
	notificationstatus text,
	numberoftries integer,
	ucmid text,
	publisher text,
	pricingtype integer,
	contenttype text,
	CONSTRAINT conprke PRIMARY KEY (id)

);
-- ddl-end --
-- object: public.country | type: TABLE --
CREATE TABLE public.country(
	id integer,
	name text,
	allowbilling boolean,
	allowshipping boolean,
	twoletterisocode varchar,
	threeletterisocode varchar,
	numberisocode integer,
	subjecttovat boolean,
	published boolean,
	displayorder integer,
	groupid integer,
	CONSTRAINT cprkcountry PRIMARY KEY (id)

);
-- ddl-end --
-- object: country_fk | type: CONSTRAINT --
ALTER TABLE public.author ADD CONSTRAINT country_fk FOREIGN KEY (id_country)
REFERENCES public.country (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --


-- object: occupation_fk | type: CONSTRAINT --
ALTER TABLE public.author ADD CONSTRAINT occupation_fk FOREIGN KEY (id_occupation)
REFERENCES public.occupation (id) MATCH FULL
ON DELETE CASCADE ON UPDATE CASCADE NOT DEFERRABLE;
-- ddl-end --



